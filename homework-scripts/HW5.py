'''
--- HW5 ---
Deadline: 22.03.2019 09:00

Using the 'ensembl_hg19.txt' file in the 'Odevler' folder (parent folder to HW5) do the following:

- Parse through the file and find the transcript with highest and lowest number of exons for EACH GENE
- Write your data to a new tab delimited file named 'HW5_results_yourname.txt' in the following format:

#GeneID Tx_with_most_exons  Tx_with_fewest_exons High_count Low_count
ENSG00000118473 ENST00000237247 ENST00000483060 27  6
ENSG00000157191 ENST00000406746 ENST00000483060 9   6
...

-First line in the new file must be a header line (see above example)
-If there are more than one transcripts of a gene with the highest or lowest number of exons, use the first transcript
 in the ensembl file.
-If there is only one transcript of a gene, use the same transcript for both fields
-If the exon count is the same for all transcripts of a gene, use the first one for both fields
-Upload the resulting .txt file and your solution .py file

TIPS:   ensembl file is tab delimited
		gene names start with ENSG
		transcript names start with ENST
		You will need to populate a list or a dictionary to keep the data while parsing through the ensembl file
		Use the resulting dictionary or list to write the new file AFTER you are done with ensembl file.
		read http://www.ensembl.org/info/genome/genebuild/genome_annotation.html to understand what is an 'ensembl gene'

'''

def func1():
    my_dict = {}
    genes_list = []
    transcript_list = []
    exon_list = []
    previous_gene = 'ENSG00000118473'

    with open('ensemble_hg19', 'r') as infh:
        next(infh)
        for line in infh:
            keys = line.split('\t')
            gene_name = keys[12]

            if gene_name == previous_gene:
                genes_list.append(keys[12])
                transcript_list.append(keys[1])
                exon_list.append(int(keys[8]))
                my_dict[gene_name] = genes_list, transcript_list, exon_list

            elif gene_name != previous_gene:
                previous_gene = gene_name
                transcript_list = []
                exon_list = []
                genes_list = []
                transcript_list.append(keys[1])
                exon_list.append(int(keys[8]))
                my_dict[gene_name] = transcript_list, exon_list



    return my_dict

func1()

def func2(dictionary):
    list_genes = []
    list= []
    for i in dictionary.values():
        genes = i[0]
        transcripts = i[1]
        exons = i[2]
        greatest = max(exons)
        smallest = min(exons)
        max_index = exons.index(greatest)
        min_index = exons.index(smallest)

        gen = genes[0]
        list_genes.append(gen)
        maximum = transcripts[max_index]
        minimum = transcripts[min_index]
        list_genes.append(maximum)
        list_genes.append(minimum)
        list_genes.append(greatest)
        list_genes.append(smallest)
        list.append(list_genes)
        list_genes = []


    return list

func2(func1())

f = open('result', 'w')
f.close()

with open('result', 'w') as infh:
    print('#GeneID Tx_with_most_exons  Tx_with_fewest_exons High_count Low_count', file=infh)
