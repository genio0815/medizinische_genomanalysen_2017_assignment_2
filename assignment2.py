#! /usr/bin/env python3

# rearranged file structure, reduced functionality to what
# is really needed; just do a single loop over file entries
# ugly but working...

import vcf
import os

__author__ = 'Alexander.Bindeus'

class Assignment2:
    def __init__(self):
        print("\nAssignment 2")
        print(__author__)
        print("using PyVCF version: %s" % vcf.VERSION)

        # hard coded input - do not care...
        vcf_reader = vcf.Reader(open(
            '/home/alex/Desktop/BioInformatik/SS_17/Medizinische_Genomanalysen/Assignments/'
            'AmpliseqExome.20141120.NA24385.vcf', 'r'))

        count = 0
        indelCount = 0
        avQualy = 0
        snpCount = 0
        hetvarCount = 0

        for record in vcf_reader:
            count = count + 1
            avQualy = avQualy + record.QUAL

            if record.is_indel:
                indelCount = indelCount + 1

            if record.is_snp:
                snpCount = snpCount + 1

            if record.num_het == 1:
                hetvarCount = hetvarCount + 1

        print('\naverage PHRED score:\t', avQualy / count)
        print('number of variants:\t', count)
        print("reference version:\t{}"
              .format(os.path.basename(vcf_reader.metadata["reference"]).strip(".fasta")))
        print('variant caller:\t', vcf_reader.metadata['source'][0])
        print('number of indels\t', indelCount)
        print('number of snvs:\t', snpCount)
        print('number of heterozygous variants\t', hetvarCount)

if __name__ == '__main__':
    assignment1 = Assignment2()



    

