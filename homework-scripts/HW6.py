'''
---=== HW7 ===---
Due date: 12.04.2019 09:00


--- PART I (0.8 pts) ---
Create a Transcript class with following attributes and methods:

Attributes:
	- Transcript ID
	- Gene ID
	- Chromosome
	- Strand
	- Number of exons
Methods:
	- 5' UTR length
	- 3' UTR length
	- Transcript length (sum of exon lengths)

You can add more attributes and methods as you see fit.
You can ignore multiexonic UTRs.

Parse through the ensembl file. Create a class instance for every transcript (i.e. "line")
collect those instances in a list.

Finally, loop through your list and print the following on the screen:
- Average 5' UTR length on + strand
- Average 5' UTR length on - strand
- Average 3' UTR length on + strand
- Average 3' UTR length on - strand
- Average transcript length
- ID of the transcript with longest 5' UTR
- ID of the transcript with longest 3' UTR

Add the following methods to your Transcript class:

- A method to construct the coding sequence using togows API (you can use other APIs too, if you like)
- A method to translate the coding sequence to amino acid sequence

Then populate a dictionary for all transcripts in Ensembl file in the following format:

{'transcript_id1' : {'cds' : 'ATGGAAACTGAG.....TGA', 'aa_seq' : 'METE....'},
 'transcript_id12 : {'cds' : 'ATG........TGA', 'aa_seq' : 'M.......'},
 ...
 }

 Then print the average CDS and aa sequence lengths on the screen

 You can use the Transcript class we have written in class or start from scratch
'''




def get_dna_seq(chrom, start, end):
    mystr = 'http://togows.org/api/ucsc/hg19/{}:{}-{}'.format(
        chrom, start, end
    )
    with urllib.request.urlopen(mystr) as response:
        html = response.read().decode("utf-8")
    return str(html)


class Transcript():
    '''
    Transcript class that calculates UTRs
    '''

    def __init__(self, name, chrom, strand, txstart, txend, cdsstart,
                 cdsend, exoncount, exonstarts, exonends, genename):
        '''
        :param name: transcript's ensembl ID
        :param chrom: chrom number (in ensembl format: chr1, chr2, chrY etc)
        :param strand: + or -
        :param txstart: transcription start coordinate
        :param txend: transcription end coordinate
        :param cdsstart: cds start coord.
        :param cdsend: cds end coord.
        :param exoncount: number of exons in the transcript
        :param exonstarts: exon start coordinates (comma seperated values. Last character should be a comma!!)
        :param exonends: exon end coordinates (comma seperated values. Last character should be a comma!!)
        :param genename: name of the gene of the transcript
        '''
        self.tx_id = name
        self.gene_id = genename
        self.chromosome_no = chrom
        self.strand = strand
        self.exon_count = int(exoncount)
        self.exon_starts = exonstarts
        self.exon_ends = exonends
        self.cds_start = int(cdsstart)
        self.cds_end = int(cdsend)
        self.tx_start = int(txstart)
        self.tx_end = int(txend)

    def exon_coords(self):
        '''
        Creates list of paired list of [start, end] for each exon
        :return: [[ex1_start, ex1_end], [ex2_start, ex2_end], ... ]
        '''
        starts = map(int, self.exon_starts[:-1].split(','))
        ends = map(int, self.exon_ends[:-1].split(','))
        return zip(starts, ends)

    def utr5(self):
        '''
        Calculates the length of 5' UTR
        :return: 5' UTR length in bases
        '''
        # if self.strand == '+':		#
        # 	return int(self.cds_start) - int(self.tx_start) + 1
        # else:
        # 	return int(self.tx_end) - int(self.cds_end) + 1

        temp = 0
        if self.strand == '+':
            for st, end in self.exon_coords():
                if self.cds_start <= end:
                    return temp + self.cds_start - end + 1
                else:
                    temp += end - st + 1

        else:
            for st, end in list(self.exon_coords())[::-1]:
                if self.cds_end >= st:
                    return temp + end - self.cds_end + 1
                else:
                    temp += end - st + 1

    def utr3(self):
        '''
        Calculates the length of 3' UTR
        :return: 3' UTR length in bases
        '''

        # if self.strand == '-':
        # 	return int(self.cds_start) - int(self.tx_start) + 1
        # else:
        # 	return int(self.tx_end) - int(self.cds_end) + 1

        temp = 0
        if self.strand == '-':

            for st, end in self.exon_coords():
                if self.cds_start <= end:
                    return temp + self.cds_start - end + 1
                else:
                    temp += end - st + 1
        else:
            for st, end in list(self.exon_coords())[::-1]:
                if self.cds_end >= st:
                    return temp + end - self.cds_end + 1
                else:
                    temp += end - st + 1

    def tx_length(self):
        '''
        Calculates transcript length
        :return: Transcript length in bases
        '''
        rv = 0
        for start, end in self.exon_coords():
            rv += end - start + 1
        return rv


# bin	1name	2chrom	3strand	4txStart	5txEnd	6cdsStart	7cdsEnd	8exonCount	9exonStarts	10exonEnds	score	12name2	cdsStartStat	cdsEndStat	exonFrames


def populate_transcripts(ens_file_path):
    '''
    Populates a list of Transcript class instances using the data from an ensembl dump
    :param ens_file_path: an ensembl dump file
    :return: list of Transcript instances
    '''
    rv = []
    with open(ens_file_path) as f:
        for line in f:
            if line.startswith('#'):
                continue
            sp = line.split('\t')
            name, chrom, strand, txstart, txend, cdsstart, cdsend, exoncount, exonstarts, exonends = sp[1:11]
            gene = sp[12]
            rv.append(Transcript(name, chrom, strand, txstart, txend, cdsstart, cdsend, exoncount, exonstarts, exonends,
                                 gene))
    return rv


fp = 'ensembl_hg19.txt'

tx_list = populate_transcripts(fp)

print(tx_list)

utr5_plus = []
utr5_minus = []
utr3_plus = []
utr3_minus = []
lengths = []
longest3 = ['', 0]
longest5 = ['', 0]

for tx in tx_list:
    utr5 = tx.utr5()
    utr3 = tx.utr3()
    if tx.strand == '+':
        utr5_plus.append(utr5)
        utr3_plus.append(utr3)
    else:
        utr5_minus.append(utr5)
        utr3_minus.append(utr3)

    lengths.append(tx.tx_length())

    if utr5 > longest5[1]:
        longest5 = [tx.tx_id, utr5]
    if utr3 > longest3[1]:
        longest3 = [tx.tx_id, utr3]

print(f"average 5' on +: {sum(utr5_plus) / len(utr5_plus)}")
print(f"average 5' on -: {sum(utr5_minus) / len(utr5_minus)}")
print(f"average 3' on +: {sum(utr3_plus) / len(utr3_plus)}")
print(f"average 3' on -: {sum(utr3_minus) / len(utr3_minus)}")
print(f"average tx length: {sum(lengths) / len(lengths)}")
print(f"longest 5' UTR: {longest5[0]} ({longest5[1]} bases)")
print(f"longest 3' UTR: {longest3[0]} ({longest3[1]} bases)")


