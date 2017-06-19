#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def meansquare(x):
    a = x[0]
    b = x[1]
    rms = math.sqrt((0.25*((a[0]-b[0])**2 + (a[1]-b[1])**2 +(a[2]-b[2])**2 + (a[3]-b[3])**2)))
    return round(rms,3)


def seqdict(filenames):
    seqs = {}
    for f in filenames:
        with open(f) as input_file:
            lines = input_file.readlines()
            start = lines.pop(0).replace("\n", "")
            sequence = ""
            for line in lines:
                line.strip()
                if line[0] == ">":
                    seqs[start] = sequence
                    sequence = ""
                else:
                    sequence += line
                    sequence = sequence.replace("N", "")
                if sequence != "":
                    seqs[start] = sequence
    return seqs

''' Main code for running of the above functions.
Ao whenver we need to fasta files to dictionary with sequence names and sequences we can easily call the above functions. The only thing we need now is
to unit test the above functions such that it is robust for different applications.
'''


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="loading fasta files")
    parser.add_argument("file", nargs='+', help='filename')
    args = parser.parse_args()
    seqs = seqdict(args.file)

    results = {}
    for [keys , seq] in seqs.items():
        counter = []
        keys_new = ((keys.split(' '))[0]).split(">")[1]
        for c in 'ATGC':
            freq = round((seq.count(c) / len(seq)),3)
            counter.append(freq)
            results[keys_new] = counter

    k = list(results.keys())
    com= list(results.values())
    l = len(k)

    for i in range(l):
        print (k[i],end = '\t')
        for j in range(l):
            test = [com[i],com[j]]
            res = meansquare(test)
            print(res, end = '\t')
        print("")