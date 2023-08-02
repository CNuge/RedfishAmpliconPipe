import os
import sys
import json
import argparse


def build_snakemake_config_samples(path=str, samples=list, suffix=str)->dict:
    """take in lists of sample names and their paths and relevant file suffix, 
        build the relevant dictonary and save to json"""
    sample_data = {}
    for x in samples:
        sample_data[x] = f"{path}{x}{suffix}"
    return {"samples": sample_data}

def write_snakemake_config(config_dict, filename="config.json", indent = 4):
    with open(filename, "w") as outfile:
        json.dump(config_dict, outfile, indent = indent)

def input_parser(args):
    parser  = argparse.ArgumentParser(prog = "Redfish Setup Script",
        description = """
        Config Creation for Redfish Amplicon Snakemake processing pipeline.\n
        This is a command line tool for setting up your config file for use with snakemake.
        """)
    parser.add_argument("-f", "--file_path", type = str, default = "data/raw_redfish_seq/", 
        help = "The path to the raw fq files for processing.")
    parser.add_argument("-s", "--suffix", type = str, default= "_R1_001.fastq.gz",
        help = "The generic suffic on the raw fq files.")
    parser.add_argument("-g", "--genome", type = str , default = "data/fasciatus_mentella_LE_fst_top50.fasta", 
        help = "The name of the genome file for alignment of reads.")
    parser.add_argument("-b", "--bcf", type = str , default = "data/calls/redfishamplicon_calls.bcf", 
        help = "The bcf file to be produced.")
    parser.add_argument("-v", "--vcf", type = str , default = "data/calls/qual_filtered_redfishamplicon_calls.vcf", 
        help = "The filtered vcf file to be produced.")
    parser.add_argument("-p", "--plink", type = str , default = "data/calls/redfishamplicon", 
        help = "The prefix for the plink bed/bim files to be produced.")
    return parser.parse_args(args)


def main():
    #parse the command line inputs
    parsed_args = input_parser(sys.argv[1:])
    sample_path = parsed_args.file_path
    sample_suffix = parsed_args.suffix
    sample_files = [x.split(sample_suffix)[0] for x in os.listdir(sample_path) if sample_suffix in x]
    snake_config_info = build_snakemake_config_samples(path=sample_path, 
                                                        samples=sample_files, 
                                                        suffix=sample_suffix)
    #add additional things to the json here
    snake_config_info["genome"] = parsed_args.genome
    snake_config_info["bcf"] = parsed_args.bcf
    snake_config_info["vcf"] = parsed_args.vcf
    
    #write the dict info to a config
    write_snakemake_config(snake_config_info)
    print("config file created, you can now run the pipeline using the snakemake commands.\n"+\
          "See README.md for details.")

if __name__ == "__main__":
    main()

