#!/usr/bin/env python2
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='Parse FASTA file.')
parser.add_argument('-f', '--fasta', dest='fasta')
args = parser.parse_args()


def tab_contigs(args):
    contigs = 0
    for record in SeqIO.parse(args.fasta, 'fasta'):  # each record contains a sequence or contig
        contigs += 1
    print ("The number of contigs is:"), contigs


def n50_fasta(args):
    lengths_list = []
    lengths_sum = 0
    for record in SeqIO.parse(args.fasta, 'fasta'):
        length = len(record.seq)
        lengths_list.append(length)
        lengths_sum += length
    lengths_list = sorted(lengths_list)
    reverse_list = lengths_list[::-1]
    half_sum = lengths_sum / 2
    contig_sum = 0

    for i in range(0, len(lengths_list)):
        if half_sum >= contig_sum:
            contig_length = reverse_list[i]
            contig_sum += contig_length
        else:
            break
    print ("The N50 of this FASTA is:"), contig_length


if __name__ == '__main__':
    tab_contigs(args)
    n50_fasta(args)