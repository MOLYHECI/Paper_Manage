## Paper_Management
A automatic script for (arxiv) papers downloading.

Download single paper

```
python main.py --mode=0 --output=Your_Output_Dir --id=arxiv_id
```
Using arxiv link as id is also valid.

I recommend using the automatic script for generating config files when you want to download many papers from arxiv. 

```
python auto_config.py --config=configs/Your_Config_Name --output=Your_Output_dir --subdir=Your_Subdir
```

Then you can type in your arxiv papers id or link.

For config-oriented downloading, using
```
python main.py --mode=1 --config=configs/Your_Config_Name
```

