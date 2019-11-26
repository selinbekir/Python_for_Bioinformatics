
def parser(myfile):
    exonend_list = []
    exonstart_list = []
    satirlar_icin =[]
    sumlar = []

    with open(myfile, 'r') as infh:
        next(infh)
        for line in infh:
            boluk = line.strip().split('\t')
            exonstart = boluk[9].split(',')
            exonstart.pop()
            exonstart = exonstart
            for i in exonstart:
                i = int(i)
                exonstart_list.append(i)

            exonend = boluk[10].split(',')
            exonend.pop()
            exonend = exonend
            for s in exonend:
                s = int(s)
                exonend_list.append(s)

            for k in range(len(exonstart_list)):
                uzunluk = exonend_list[k] - exonstart_list[k]
                satirlar_icin.append(uzunluk)
            sumlar.append(sum(satirlar_icin))

            satirlar_icin = []
            exonstart_list = []
            exonend_list = []

    return sumlar


def averager(listem):
    mysum = 0
    for i in listem:
        mysum = mysum + i
    return mysum / len(listem)

print(averager(parser('ensembl_hg19.txt')))
