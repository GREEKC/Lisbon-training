# Finding motif by UniprotID or Gene name

Lets get motif (matrix) for an AR gene in human (ANDR_HUMAN protein). To match the exact name we use regexp embraced by line start and line stop anchors `^AR$` or `^ANDR_HUMAN.` (comma separates protein name from the next part of motif name):
```
http://hocomoco11.autosome.ru/search.json?arity=mono&species=human&query=^AR$
http://hocomoco11.autosome.ru/search.json?arity=mono&species=human&query=^ANDR_HUMAN\.
```

You get a list of motifs:
```
["ANDR_HUMAN.H11MO.0.A","ANDR_HUMAN.H11MO.1.A","ANDR_HUMAN.H11MO.2.A"]
```

Take each of them and put its name into a pair of requests:
* To get general information: `http://hocomoco11.autosome.ru/motif/ANDR_HUMAN.H11MO.0.A.json`
* To get PWM motif: `http://hocomoco11.autosome.ru/motif/ANDR_HUMAN.H11MO.0.A/pwm.json`
* To get PCM motif: `http://hocomoco11.autosome.ru/motif/ANDR_HUMAN.H11MO.0.A/pcm.json`

First request results into an JSON object:
```javascript
{
	"full_name":"ANDR_HUMAN.H11MO.0.A",
	"direct_logo_url":"/final_bundle/hocomoco11/full/HUMAN/mono/logo_large/ANDR_HUMAN.H11MO.0.A_direct.png",
	"revcomp_logo_url":"/final_bundle/hocomoco11/full/HUMAN/mono/logo_large/ANDR_HUMAN.H11MO.0.A_revcomp.png",
	"gene_names":["AR"],
	"model_length":18,
	"rank":0,
	"quality":"A",
	"consensus":"WKThYYddbhTRTTTRYh",
	"motif_source":"ChIP-Seq",
	"release":"HOCOMOCOv11",
	"best_auc_human":0.9598370988250885,
	"best_auc_mouse":0.8107911506420812,
	"num_datasets_human":461,
	"num_datasets_mouse":57,
	"num_words_in_alignment":499,
	"motif_families":["Steroid hormone receptors (NR3){2.1.1}"],
	"motif_subfamilies":["GR-like receptors (NR3C){2.1.1.1}"],
	"hgnc_ids":["644"],
	"entrezgene_ids":["367"],
	"uniprot_id":"ANDR_HUMAN",
	"uniprot_acs":["P10275"],
	"comment":"",
	"retracted":false
}

```
The latter requests give you matrices Nx4, each position encodes scores/counts for A,C,G,T nucleotides in that exact order. For example, PWM is the following:
```javascript
[
  [ -0.5138485794665265, -1.2399175742449602, -1.8655485050187224, 1.084375319343181 ],
  [ -1.3558107967490831, -1.5979243253691162, 1.126315335180832, -0.7859760865669171 ],
  [ -1.2676561789463086, -1.296186219352633, -2.692385167405107, 1.2170520000031797 ],
  [ -0.27900232860428914, -0.36643892679792994, -0.5406766868713487, 0.6769717303692195 ],
  [ -1.1360714847313766, 1.0681829564633654, -1.8655485050187224, -0.48772145432535496 ],
  [ -0.7026683620092956, 0.1069007381681436, -1.9734514739247802, 0.8122350787253819 ],
  [ -0.32176528712710334, -0.6110756026861811, -0.23799329402059072, 0.6648284452249204 ],
  [ -0.22799852314755842, -0.3327479937648922, -0.1422751481965396, 0.482142869635976 ],
  [ -0.34385266094413197, -0.2582876084265846, -0.11525941366682767, 0.4870196636500838 ],
  [ -0.21810265997474643, 0.025406251683139865, -0.7187839277455842, 0.5205071001782793 ],
  [ -1.2129276783070357, -2.692385167405107, -2.692385167405107, 1.2717910717651395 ],
  [ 0.017657467621501614, -2.0321084736269577, 1.0093512205888326, -2.2320658766542025 ],
  [ -2.094421693288641, -2.308713230230392, -2.3917267227648282, 1.3045412900468412 ],
  [ -2.482260443767237, -3.3228653459083506, -0.9156596935183965, 1.2470736644300016 ],
  [ -3.1243193729807612, -3.1243193729807612, -1.325554187582936, 1.2937432886393043 ],
  [ 0.5157912926269675, -2.0944216932886413, 0.6769717303692194, -1.4524945930071118 ],
  [ -1.0420020890358872, 0.7355700794745771, -1.5979243253691164, 0.30620815828392317 ],
  [ 0.14870318996623036, -0.4497677478067023, -1.4869176655913858, 0.6809869429347905 ]
]
```

One can also filter motifs by quality (A,B,C consist reliable core of HOCOMOCO, D-quality motifs are less reliable). If one want to take the only motif, use a primary one (one which has rank equals to 0).

# Documentation page
A bit more details are available on the following [page](http://hocomoco11.autosome.ru/api_description)
