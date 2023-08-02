# RedfishAmpliconPipe
A snakemake pipeline for processing and snp calling of amplicon data for redfish species identification.

Please note this is a work in progress, documentation will be updated with time.


## Setup / Installation

The easiest way to set up the snakemake environment is with conda. The commands below should help you get started, but exact setup may vary depending on your environment.

```

##
# build the conda env
conda install -n base -c conda-forge mamba
conda activate base
mamba create -c conda-forge -c bioconda -n snakemake snakemake

##
# activate the snakemake env
conda activate snakemake

pip install pysam
pip install matplotlib

##
# configure the channels and install the binf packages needed (into the snakemake environment)
conda config --env --add channels defaults
conda config --env --add channels bioconda
conda config --env --add channels conda-forge

# install the necessary software
conda install fastp
```
On subsequent executions you can simply run the following to activate the snakemake env
```
conda activate snakemake
```


##  Pipeline

### Setup the workflow

Once inputs are provided, we build a config file

```
python redfish_snake_setup.py 
```

### Commands for execution of Amplicon calling Snakemake workflow

```
#execute the snakemake file

#dry run to test procedure
snakemake --snakefile RedfishMarkerCall -np

#make a diagram of the process
snakemake --dag  | dot -Tsvg > redfish_pipeline.svg #make a diagram of it

# run the whole pipeline
snakemake --cores

# run specific rules
snakemake -R fastp_cut -n #-n makes it a dry run

```

Individual steps listed below:

```
snakemake --snakefile RedfishMarkerCall -R fastp_cut 
snakemake --snakefile RedfishMarkerCall -R bwa_index 
snakemake --snakefile RedfishMarkerCall -R bwa_map
snakemake --snakefile RedfishMarkerCall -R samtools_sort
snakemake --snakefile RedfishMarkerCall -R samtools_index
snakemake --snakefile RedfishMarkerCall -R bcftools_call
snakemake --snakefile RedfishMarkerCall -R variant_filter
```

### Commands for execution of Plink conversion Snakemake workflow

```
```
#execute the snakemake file

#dry run to test procedure
snakemake --snakefile PlinkSnakefile -np

snakemake --snakefile PlinkSnakefile --cores


```

## Tests

There are five example files and the reference panel included within the `data/` folder. These allows for a small test run of the pipeline to be conducted.

