
'''
Create a text file called deneme.txt. A tab delimited file with two columns.
#Name surname (header line, ignore this line)
Ahmet    Veli
Mehmet    Topaloglu
Ali    Gel

Calculate the number of rows where the length of the surname is larger than the length of the name.

For the above example your program must print 1 to the screen because the above condition is valid only for the 2nd row.

Please note that, the text file can have thousands of rows.

It is obligatory to write at least one FRUITFUL function
'''


with open('deneme.txt', 'w') as outfh:
    print('Ahmet\tVeli\nMehmet\tTopaloglu\nAli\tGel', file=outfh)

def parser(dosyam):
    list = []
    with open (dosyam, 'r') as infh:
        for line in infh:
            if line.startswith('#'):
                continue
            boluk = line.strip().split('\t')
            isim = boluk[0]
            soyisim = boluk[1]
            if len(soyisim) > len(isim):
                list.append(isim)
    return len(list)

print(parser('deneme.txt'))
