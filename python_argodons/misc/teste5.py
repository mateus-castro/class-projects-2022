from itertools import count


bla1 = ['cucu', 'lerolero']
bla2 = ['suvao', 'banho', 'suvao']
count = 0
bla3 = []
while count < 4:
    bla3+=bla2
    count += 1

# print(list(filter(('suvao').__ne__, bla2)))
print(','.join(bla2))