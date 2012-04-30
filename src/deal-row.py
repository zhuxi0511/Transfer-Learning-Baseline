#!/usr/bin/python

import sys

fin = file(sys.argv[1])
fout = file(sys.argv[2], 'w')

for line in fin:
	tmp = []
	if len(line) != 0:
		spli = line.split()
		for i in range(len(spli)):
			if i != 1:
				tmp.append(spli[i])
				if ( i != len(spli) - 1 ):
					tmp.append('\t')
	fout.writelines(tmp)
	fout.write('\n')

fin.close();
fout.close();
	


