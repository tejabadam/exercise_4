import argparse
import math

'''Exercise from the group

Modified by Sailen P based on original codes by Tejabadam

Status : Does the work outlined howver issues with the output as it doesnot output as input; something wrong with dictionary creation
         Unit testing needs to be done 
         Functional module needs to be done
         Version 1 
 '''

def meansquare(x):
    a = x[0]
    b = x[1]
    rms = math.sqrt((0.25*((a[0]-b[0])**2 + (a[1]-b[1])**2 +(a[2]-b[2])**2 + (a[3]-b[3])**2)))
    return (round(rms,3))


parser = argparse.ArgumentParser(description="loading fasta files")
parser.add_argument("file", nargs='+', help='filename')
args = parser.parse_args()


seqs = {}
for f in args.file:
    with open(f) as input_file:
        lines = input_file.readlines()
        start = lines.pop(0).replace("\n", "")
        sequence = ""
        for line in lines:
            if line[0] == ">":
                seqs[start] = sequence
                sequence = ""
                start = line.replace("\n", "")
            else:
                sequence += line.replace("\n", "")
                sequence = sequence.replace("N", "")
        if sequence != "":
            seqs[start] = sequence


results = {}
for [keys, seq] in seqs.items():
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
    print (k[i],end ="\t")
    for j in range(l):
        test = [com[i],com[j]]
        res = meansquare(test)
        print (res, end = "\t")
    print ("")



