# dictionary maps:
# chr1-chr23 to 1-23
# X to 23
# Y to 24
# M and MT to 25
# chromosomes = [[str(x)] for x in range(1, 23)] + [['X'], ['Y'], ['MT', 'M']]
# chromosomes = {'chr' + x: y for l, y in zip(chromosomes, range(1, 1000)) for x in l}
# print(chromosomes)

chromosomes = {'chr1': 1, 'chr2': 2, 'chr3': 3, 'chr4': 4, 'chr5': 5,
               'chr6': 6, 'chr7': 7, 'chr8': 8, 'chr9': 9, 'chr10': 10,
               'chr11': 11, 'chr12': 12, 'chr13': 13, 'chr14': 14, 'chr15': 15,
               'chr16': 16, 'chr17': 17, 'chr18': 18, 'chr19': 19, 'chr20': 20,
               'chr21': 21, 'chr22': 22, 'chrX': 23, 'chrY': 24, 'chrMT': 25, 'chrM': 25}
