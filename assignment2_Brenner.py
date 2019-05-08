#! /usr/bin/env python3

import vcf

__author__ = 'Stefan Brenner'


class Assignment2:
    
    def __init__(self):
        print("PyVCF version: %s" % vcf.VERSION,"\n")

    def get_average_quality_of_file(self):

        total = 0
        record_quality = 0
        read_file = vcf.Reader(open('chr22_new.vcf','r'))

        for record in read_file:
            total += 1
            record_quality += record.QUAL
        average_quality = record_quality/total
        print("Average quality of file: ", average_quality,"\n")

        
    def get_total_number_of_variants_of_file(self):

        total = 0
        read_file = vcf.Reader(open('chr22_new.vcf','r'))

        for record in read_file:
           total += 1
        print("Total number of variants of file: ", total,"\n")

    def get_variant_caller_of_vcf(self):

        variant_caller = []
        read_file = vcf.Reader(open('chr22_new.vcf','r'))

        for record in read_file:
            variant_caller = record.INFO['callsetnames']
        print("Variant caller: ", variant_caller[1],"\n")

    def get_human_reference_version(self):

        read_file = vcf.Reader(open('chr22_new.vcf','r'))

        print("Human reference version: hg38","\n",read_file.metadata,"\n")
        
    def get_number_of_indels(self):

        indels = 0
        read_file = vcf.Reader(open('chr22_new.vcf','r'))

        for record in read_file:
            if record.is_indel:
                indels += 1
        print('Number of indels: ', indels,"\n")

    def get_number_of_snvs(self):


        snv = 0
        read_file = vcf.Reader(open('chr22_new.vcf','r'))

        for record in read_file:
            if record.is_snp:
                snv += 1
        print('Number of snvs: ', snv, "\n")
        
    def get_number_of_heterozygous_variants(self):

        heterozygous_variants = 0
        read_file = vcf.Reader(open('chr22_new.vcf','r'))


        for record in read_file:
            if record.num_het:
                heterozygous_variants += 1
        print('Number of heterozygous variants: ',heterozygous_variants,"\n")

    def merge_chrs_into_one_vcf(self):


        print("Number of total variants: TODO","\n")

    
    def print_summary(self):
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()

    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



