#!/usr/bin/env perl

# Sample script to access several Ensembl REST endpoints with a sequence of requests
# Adapted from the sample client offered at https://github.com/Ensembl/ensembl-rest/wiki/Example-Perl-Client
# Other language examples are available on the same site

use Modern::Perl;
use HTTP::Tiny;
use Time::HiRes;
use JSON;
use Data::Dumper;

my $http = HTTP::Tiny->new();
my $server = 'http://rest.ensembl.org';
my $global_headers = { 'Content-Type' => 'application/json' };
my $last_request_time = Time::HiRes::time();
my $request_count = 0;

run();

sub run {
  my ($species, $region) = @ARGV;
  $species ||= 'human';
  $region ||= '10:30012800-30059524';
  
  # find any genes overlapping a given coordinate range
  my $response = perform_json_action(
    '/overlap/region/'.$species.'/'.$region,
    [
      ['feature','gene']
    ]);
  print Dumper $response;

  # Get the gene ID from the response and use that to get the relevant sequence
  my $gene_id = $response->[0]->{id};
  $response = perform_json_action(
    '/sequence/id/'.$gene_id,
    [
      ['Content-Type','text/x-fasta'],
      ['expand_5prime',1000]  # include upstream 1kb of sequence
    ]);
  print $response->{seq}."\n";
  

  # Get regulatory features around the coordinates of the gene

  $response = perform_json_action(
    '/overlap/region/'.$species.'/'.$region,
    [
      ['feature','regulatory']
    ]);
  print Dumper $response;

  # Filter for a particular epigenome activity 
  my @promoters = grep { $_->{activity}->{M0_macrophage_CB} eq 'POISED' } @$response;

  # ...and query the regulation endpoint for additional activity data
  foreach my $element (@$response) {
    my $id = $element->{ID};
    $response = perform_json_action(
      '/regulatory/species/'.$species.'/id/'.$id,
      [
        ['activity',1]
      ]);
    print Dumper $response;
  }

  # What about variants and phenotypes associated with this region?

  $response = perform_json_action(
    "$species/$region",
    [
      ['feature_type','Variation'],
      ['only_phenotype',1]
    ]
    );
  print Dumper $response;

  return;
}

# Wrapper which unpacks JSON documents from rest.ensembl.org into Perl structures
sub perform_json_action {
  my ($endpoint, $parameters) = @_;
  my $headers = $global_headers;
  my $content = perform_rest_action($endpoint, $parameters, $headers);
  return {} unless $content;
  my $json = decode_json($content);
  return $json;
}

# Utilty function to send requests to rest.ensembl.org and react to errors or rate limiting
sub perform_rest_action {
  my ($endpoint, $parameters, $headers) = @_;
  $parameters ||= [];
  $headers ||= {};
  $headers->{'Content-Type'} = 'application/json' unless exists $headers->{'Content-Type'};
  if($request_count == 15) { # check every 15
    my $current_time = Time::HiRes::time();
    my $diff = $current_time - $last_request_time;
    # if less than a second then sleep for the remainder of the second
    if($diff < 1) {
      Time::HiRes::sleep(1-$diff);
    }
    # reset
    $last_request_time = Time::HiRes::time();
    $request_count = 0;
  }
  
  my $url = $server.$endpoint;
  
  if(@$parameters) {
    my @params;
    foreach my $pair (@$parameters) {
      push(@params, $pair->[0].'='.$pair->[1]);      
    }
    
    my $param_string = join(';', @params);
    $url.= '?'.$param_string;
  }
  my $response = $http->get($url, {headers => $headers});
  my $status = $response->{status};
  if(!$response->{success}) {
    # Quickly check for rate limit exceeded & Retry-After (lowercase due to our client)
    if($status == 429 && exists $response->{headers}->{'retry-after'}) {
      my $retry = $response->{headers}->{'retry-after'};
      Time::HiRes::sleep($retry);
      # After sleeping see that we re-request
      return perform_rest_action($endpoint, $parameters, $headers);
    }
    else {
      my ($status, $reason) = ($response->{status}, $response->{reason});
      die "Failed for $endpoint! Status code: ${status}. Reason: ${reason}\n";
    }
  }
  $request_count++;
  if(length $response->{content}) {
    return $response->{content};
  }
  return;
}
