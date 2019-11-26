'''Using the seqlist and enzlist tuples below, find the positions of first base of the first recognition site and total
number of recognition sites for each enzyme in human, chimpanzee and mouse beta actin coding sequences. Remember that
python gives the first position as 0 and not 1, and you should correct it in your output.

Requirements:

1- You are required to write at least two functions:
	- One to find the recognition sites and returns a list of lists in the following format:
		[
		 ['Human ACTB',      [['EcoRI', 0], ['XbaI', 0], ['EcoRV', 10,1], ['DpnI', 363, 7], ['SmaI', 80, 1]],
		 ['Chimpanzee Actb', [['EcoRI', 0], ['XbaI', 0], ['EcoRV', 10,1], ['DpnI', 282, 8], ['SmaI', 80, 1]],
		 ... ]
	- One to print the data created by the first function.
	- You can split any of the above functions into multiple functions should you deem necessary.

2- Do NOT use the built-in find function. Do the search with for loops you write yourselves.

3- Do not hard-code the enzyme list. Your code should work with enzymes that are currently not in the list.

4- Format your print function to print something similar to the following output:

----- Human ACTB ------
EcoRI : no recognition sites
XbaI : no recognition sites
EcoRV : first recognition site start position: 10 ,total recognition sites: 1
DpnI : first recognition site start position: 363 ,total recognition sites: 7
SmaI : first recognition site start position: 80 ,total recognition sites: 1
----- Chimpanzee Actb ------
EcoRI : no recognition sites
XbaI : no recognition sites
EcoRV : first recognition site start position: 10 ,total recognition sites: 1
DpnI : first recognition site start position: 252 ,total recognition sites: 8
SmaI : first recognition site start position: 80 ,total recognition sites: 1
----- Mouse Actb ------
EcoRI : no recognition sites
XbaI : first recognition site start position: 660 ,total recognition sites: 1
EcoRV : first recognition site start position: 10 ,total recognition sites: 1
DpnI : first recognition site start position: 252 ,total recognition sites: 7
SmaI : first recognition site start position: 80 ,total recognition sites: 1
'''

# EcoRI: GAATTC
# XbaI: TCTAGA
# EcoRV: GATATC
# DpnI: GATC
# SmaI: CCCGGG

seqlist = (
		   ('Human ACTB','ATGGATGATGATATCGCCGCGCTCGTCGTCGACAACGGCTCCGGCATGTGCAAGGCCGGCTTCGCGGGCGACGATGCCCCCCGGGCCGTCTTCCCCTCCATCGTGGGGCGCCCCAGGCACCAGGGCGTGATGGTGGGCATGGGTCAGAAGGATTCCTATGTGGGCGACGAGGCCCAGAGCAAGAGAGGCATCCTCACCCTGAAGTACCCCATCGAGCACGGCATCGTCACCAACTGGGACGACATGGAGAAAATCTGGCACCACACCTTCTACAATGAGCTGCGTGTGGCTCCCGAGGAGCACCCCGTGCTGCTGACCGAGGCCCCCCTGAACCCCAAGGCCAACCGCGAGAAGATGACCCAGATCATGTTTGAGACCTTCAACACCCCAGCCATGTACGTTGCTATCCAGGCTGTGCTATCCCTGTACGCCTCTGGCCGTACCACTGGCATCGTGATGGACTCCGGTGACGGGGTCACCCACACTGTGCCCATCTACGAGGGGTATGCCCTCCCCCATGCCATCCTGCGTCTGGACCTGGCTGGCCGGGACCTGACTGACTACCTCATGAAGATCCTCACCGAGCGCGGCTACAGCTTCACCACCACGGCCGAGCGGGAAATCGTGCGTGACATTAAGGAGAAGCTGTGCTACGTCGCCCTGGACTTCGAGCAAGAGATGGCCACGGCTGCTTCCAGCTCCTCCCTGGAGAAGAGCTACGAGCTGCCTGACGGCCAGGTCATCACCATTGGCAATGAGCGGTTCCGCTGCCCTGAGGCACTCTTCCAGCCTTCCTTCCTGGGCATGGAGTCCTGTGGCATCCACGAAACTACCTTCAACTCCATCATGAAGTGTGACGTGGACATCCGCAAAGACCTGTACGCCAACACAGTGCTGTCTGGCGGCACCACCATGTACCCTGGCATTGCCGACAGGATGCAGAAGGAGATCACTGCCCTGGCACCCAGCACAATGAAGATCAAGATCATTGCTCCTCCTGAGCGCAAGTACTCCGTGTGGATCGGCGGCTCCATCCTGGCCTCGCTGTCCACCTTCCAGCAGATGTGGATCAGCAAGCAGGAGTATGACGAGTCCGGCCCCTCCATCGTCCACCGCAAATGCTTCTAG'),
           ('Chimpanzee Actb', 'ATGGATGATGATATCGCCGCGCTCGTTGTCGACAACGGCTCCGGCATGTGCAAGGCCGGCTTCGCGGGCGACGATGCCCCCCGGGCCGTCTTCCCCTCCATCGTGGGGCGCCCCAGGCACCAGGGCGTGATGGTGGGCATGGGTCAGAAGGATTCCTATGTGGGCGACGAGGCCCAGAGCAAGAGAGGCATCCTCACCCTGAAGTACCCTATCGAGCACGGCATCGTCACCAACTGGGACGACATGGAGAAGATCTGGCACCACACCTTCTACAATGAGCTGCGTGTGGCTCCCGAGGAGCACCCCGTGCTGCTCACCGAGGCCCCCCTGAACCCCAAGGCCAACCGCGAGAAGATGACCCAGATCATGTTTGAGACCTTCAACACCCCAGCCATGTACGTTGCTATCCAGGCTGTGCTATCCCTGTACGCCTCTGGCCGTACCACTGGCATCGTGATGGACTCCGGTGACGGGGTCACCCACACTGTGCCCATCTACGAGGGGTATGCCCTCCCCCATGCCATCCTGCGTCTGGACCTGGCTGGCCGGGACCTGACTGACTACCTCATGAAGATCCTCACCGAGCGCGGCTACAGCTTCACCACCACGGCCGAGCGGGAAATCGTGCGTGACATTAAGGAGAAGCTGTGCTACGTCGCCCTGGACTTCGAGCAGGAGATGGCCACGGCTGCTTCCAGCTCCTCCCTGGAGAAGAGCTACGAGCTGCCTGACGGCCAGGTCATCACCATTGGCAATGAGCGGTTCCGCTGCCCTGAGGCACTCTTCCAGCCTTCCTTCCTGGGCATGGAGTCCTGTGGCATCCACGAAACTACCTTCAACTCCATCATGAAGTGTGACGTGGACATCCGCAAAGACCTGTACGCCAACACAGTGCTGTCTGGCGGCACCACCATGTACCCTGGCATCGCCGACAGGATGCAGAAGGAGATCACTGCCCTGGCACCCAGCACAATGAAGATCAAGATCATTGCTCCTCCTGAGCGCAAGTACTCCGTGTGGATCGGCGGCTCCATCCTGGCCTCGCTGTCCACCTTCCAGCAGATGTGGATCAGCAAGCAGGAGTATGACGAGTCCGGCCCCTCCATCGTCCACCGCAAATGCTTCTAG'),
           ('Mouse Actb', 'ATGGATGACGATATCGCTGCGCTGGTCGTCGACAACGGCTCCGGCATGTGCAAAGCCGGCTTCGCGGGCGACGATGCTCCCCGGGCTGTATTCCCCTCCATCGTGGGCCGCCCTAGGCACCAGGGTGTGATGGTGGGAATGGGTCAGAAGGACTCCTATGTGGGTGACGAGGCCCAGAGCAAGAGAGGTATCCTGACCCTGAAGTACCCCATTGAACATGGCATTGTTACCAACTGGGACGACATGGAGAAGATCTGGCACCACACCTTCTACAATGAGCTGCGTGTGGCCCCTGAGGAGCACCCTGTGCTGCTCACCGAGGCCCCCCTGAACCCTAAGGCCAACCGTGAAAAGATGACCCAGATCATGTTTGAGACCTTCAACACCCCAGCCATGTACGTAGCCATCCAGGCTGTGCTGTCCCTGTATGCCTCTGGTCGTACCACAGGCATTGTGATGGACTCCGGAGACGGGGTCACCCACACTGTGCCCATCTACGAGGGCTATGCTCTCCCTCACGCCATCCTGCGTCTGGACCTGGCTGGCCGGGACCTGACAGACTACCTCATGAAGATCCTGACCGAGCGTGGCTACAGCTTCACCACCACAGCTGAGAGGGAAATCGTGCGTGACATCAAAGAGAAGCTGTGCTATGTTGCTCTAGACTTCGAGCAGGAGATGGCCACTGCCGCATCCTCTTCCTCCCTGGAGAAGAGCTATGAGCTGCCTGACGGCCAGGTCATCACTATTGGCAACGAGCGGTTCCGATGCCCTGAGGCTCTTTTCCAGCCTTCCTTCTTGGGTATGGAATCCTGTGGCATCCATGAAACTACATTCAATTCCATCATGAAGTGTGACGTTGACATCCGTAAAGACCTCTATGCCAACACAGTGCTGTCTGGTGGTACCACCATGTACCCAGGCATTGCTGACAGGATGCAGAAGGAGATTACTGCTCTGGCTCCTAGCACCATGAAGATCAAGATCATTGCTCCTCCTGAGCGCAAGTACTCTGTGTGGATCGGTGGCTCCATCCTGGCCTCACTGTCCACCTTCCAGCAGATGTGGATCAGCAAGCAGGAGTACGATGAGTCCGGCCCCTCCATCGTGCACCGCAAGTGCTTCTAG')
		  )
enzlist = (
		   ('EcoRI', 'GAATTC'),
           ('XbaI', 'TCTAGA'),
           ('EcoRV', 'GATATC'),
           ('DpnI', 'GATC'),
           ('SmaI', 'CCCGGG')
		  )

####for the ENZYME EcoRI 'GAATTC'######

def recognitionsite(seqlist):
    human = []
    chimp = []
    mouse = []
    s = ''
    counter1 = 0  # totaloccurance
    counter2 = 0  # firstoccurance
    first_occurance = 0

    occured = False

    for i in seqlist[0][1]:
        counter2 += 1
        s += i
        if 'GAATC' in s:
            if occured == False:
                first_occurance = counter2
            occured = True
            counter1 += 1
            s = ''
    return first_occurance , counter1

print('---Human, EcoRI, First and total occurances: ')
print(recognitionsite(seqlist))



#### a better approach ######

def seq_finder(gene_seq, enz_seq):
    '''finds occurences of seqA in seqB
    returns a list of positions'''
    rv = []
    for idx in range(len(gene_seq)):
        if gene_seq[idx : idx + len(enz_seq)] == enz_seq:
            rv.append(idx)
    return rv

#[
		 # ['Human ACTB',      [['EcoRI', 0], ['XbaI', 0], ['EcoRV', 10,1], ['DpnI', 363, 7], ['SmaI', 80, 1]],
		 # ['Chimpanzee Actb', [['EcoRI', 0], ['XbaI', 0], ['EcoRV', 10,1], ['DpnI', 282, 8], ['SmaI', 80, 1]],
		 # ... ]
def listeleyici(gene_list, enz_list):
    '''gives the required list format'''
    rv = []
    for tpl in gene_list:
        gene_name = tpl[0]
        gene_seq = tpl[1]
        g_list = [gene_name]
        bl = []

        for tpl_enz in enz_list:
            enz_name = tpl_enz[0]
            enz_seq = tpl_enz[1]
            pos_list = seq_finder(gene_seq, enz_seq)
            if len(pos_list) > 0:
                e_list = [enz_name, pos_list[0] +1, len(pos_list)]
            else:
                e_list = [enz_name, 0]
            bl.append(e_list)

        g_list.append(bl)
        rv.append(g_list)
    return rv


def yazici(result_list):
    '''printing the output of listeleyici function, in the required format'''
    for gene_result in result_list:
        #['Human ACTB', [['EcoRI', 0], ['XbaI', 0], ['EcoRV', 10, 1], ['DpnI', 363, 7], ['SmaI', 80, 1]]]
        gene_name = gene_result[0]
        print('-----', gene_name, '------')
        enz_list = gene_result[1]
        for enz in enz_list:
            # ['EcoRV', 10, 1]
            #['XbaI', 0]
            if enz[1] == 0:
                print(enz[0], ': no recognition sites')
            else:
                print(enz[0], ': first recognition site start position:', enz[1] ,',total recognition sites:',
                      enz[2])
                # print(f'{enz[0]}: first recognition site start position: {enz[1]}, total recognition sites: {enz[2]}')


yazici(listeleyici(seqlist, enzlist))



