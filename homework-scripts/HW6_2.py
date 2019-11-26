

'''
--- PART II (0.2 pts) ---

Using some_UTRs.txt file, find the restriction sites of type II restriction enzymes listed below in sequences
in the file and print the results to a file in the following tab delimited format:

transcriptID1	name_of_the_enzyme_1	matched_pattern1	number of matches
transcriptID1	name_of_the_enzyme_1	matched_pattern2	number of matches
transcriptID2	name_of_the_enzyme_2	matched_pattern1	number of matches
transcriptID3	name_of_the_enzyme_3	matched_pattern1	number of matches
...


List of restriction enzymes:
Name	Recognition sequence
EcoRII	CCWGG
AvaII	GGWCC
HindII	GTYRAC
NspI	RCATGY

Use the following table to write regular expressions

Symbol	Meaning
G	G
A	A
T	T
C	C
R	G or A
Y	T or C
M	A or C
K	G or T
S	G or C
W	A or T
H	A or C or T
B	G or T or C
V	G or C or A
D	G or A or T
N	G or A or T or C
'''

import re

# regular expressions for restriction enzymes
motifs = {'EcoRII': 'CC[AT]GG',
          'AvaII': 'GG[AT]CC',
          'HindII': 'GT[TC][GA]AC',
          'NspI': '[GA]CATG[TC]'}

fp = 'some_UTRs.txt' #path of the file

with open(fp) as f:
    for line in f:
        tx_id, seq = line.split('\t') # get tx_id and sequence
        for motif in motifs: # loop through the motifs dict above
            matches = re.findall(motifs[motif], seq) # use findall to get a list of matched patterns
            match_dict = {x: matches.count(x) for x in matches} # create a dictionary {matched_pattern : match_count, ...}
            # lines below are for printing in required format
            for match in match_dict:
                print(f'{tx_id}\t{motif}\t{match}\t{match_dict[match]}')

