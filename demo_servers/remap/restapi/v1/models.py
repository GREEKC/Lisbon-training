# -*- coding: utf-8 -*-
## Author: Aziz Khan
## License: GPL v3
## Copyright © 2017 Aziz Khan <azez.khan__AT__gmail.com>

from __future__ import unicode_literals

from django.db import models


class Ct(models.Model):
    cellular_type = models.CharField(db_column='Cellular_Type', primary_key=True, max_length=20)  # Field name made lowercase.
    public_number = models.IntegerField(blank=True, null=True)
    encode_number = models.IntegerField(blank=True, null=True)
    bto_id = models.CharField(db_column='BTO_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    information = models.CharField(db_column='Information', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    cell_name = models.CharField(db_column='Cell_name', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    aliases = models.CharField(db_column='Aliases', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    link_ebi = models.CharField(db_column='Link_ebi', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    other_link = models.CharField(db_column='Other_link', max_length=10000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT'


class Gse(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    transcription_factor = models.CharField(db_column='Transcription_Factor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cellular_type = models.CharField(db_column='Cellular_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modification_tf = models.CharField(db_column='Modification_TF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modification_ct = models.CharField(db_column='Modification_CT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_gse = models.CharField(db_column='ID_GSE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)  # Field name made lowercase.
    encode = models.CharField(db_column='Encode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    filter_macs = models.CharField(db_column='Filter_macs', max_length=3, blank=True, null=True)  # Field name made lowercase.
    total_map = models.IntegerField(db_column='Total_map', blank=True, null=True)  # Field name made lowercase.
    mapped = models.IntegerField(db_column='Mapped', blank=True, null=True)  # Field name made lowercase.
    multi_mapped = models.IntegerField(db_column='Multi_mapped', blank=True, null=True)  # Field name made lowercase.
    unmapped = models.IntegerField(db_column='Unmapped', blank=True, null=True)  # Field name made lowercase.
    peaks_filter_macs = models.IntegerField(db_column='Peaks_filter_macs', blank=True, null=True)  # Field name made lowercase.
    peaks_initial_macs = models.IntegerField(db_column='Peaks_initial_macs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GSE'


class Tf(models.Model):
    transcription_factor = models.CharField(db_column='Transcription_Factor', primary_key=True, max_length=10)  # Field name made lowercase.
    superclass = models.CharField(db_column='SuperClass', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    family = models.CharField(db_column='Family', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subfamily = models.CharField(db_column='SubFamily', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description_uniprot = models.CharField(db_column='Description_Uniprot', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=25, blank=True, null=True)  # Field name made lowercase.
    aliases = models.CharField(db_column='Aliases', max_length=200, blank=True, null=True)  # Field name made lowercase.
    chr_localisation = models.CharField(db_column='Chr_localisation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function = models.CharField(db_column='Function', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    uniprot = models.CharField(db_column='Uniprot', max_length=100, blank=True, null=True)  # Field name made lowercase.
    refseq = models.CharField(db_column='RefSeq', max_length=800, blank=True, null=True)  # Field name made lowercase.
    ensembl = models.CharField(db_column='Ensembl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    tfe_id = models.CharField(db_column='TFe_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_wikigene = models.CharField(db_column='Link_wikigene', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_jaspar = models.CharField(db_column='Link_jaspar', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_wikipedia = models.CharField(db_column='Link_wikipedia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_fb = models.CharField(db_column='Link_FB', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TF'