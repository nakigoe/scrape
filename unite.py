#unite several *.txt files with emails into one file and remove duplicates:

import os, glob
files = glob.glob('*.txt')

all_lines = []
for f in files:
    with open(f,'r') as fi:
        all_lines += fi.readlines()
all_lines = set(all_lines)

with open('combinedfile.txt','w') as fo:
    fo.write("".join(all_lines))