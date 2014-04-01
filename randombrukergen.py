import random
from collections import OrderedDict

data = []

f1 = open('rnames.txt', 'r')
f2 = open('rplaces.txt', 'r')

for i, e in enumerate(zip(f1, f2)):
    
    navn = e[0]
    navn = navn.split()
    adresse = e[1]
    adresse = adresse.split()
    adresse[0] = adresse[0].replace(',','')
    adresse[1]= adresse[1].replace(',','')
    adresse[3] = adresse[3].replace(',','')

    print adresse
    persondata = OrderedDict()
    persondata['id'] = random.randint(10,100000)
    persondata['rettighet'] = 'INTRO'
    persondata['fornavn'] = navn[0]
    persondata['etternavn'] = navn[1]
    persondata['personnr'] = random.randint(10000000000, 99999999999)
    persondata['DUFnr'] = random.randint(10000000000, 99999999999)
   
    persondata['bostedsadresse'] = adresse[1] + " " + adresse[0]
    persondata['postnummer'] = random.randint(1100,9999)
    persondata['sted'] = adresse[3]

    persondata['RPNo'] = random.randint(0,200)
    persondata['s50'] = random.randint(0,200)
    persondata['NBeh'] = random.randint(0,200)
    data.append(persondata)


import csv
        
f3 = open('indata.csv','w')
writer = csv.writer(f3)  

e = data[0]
    #print e
row = []
for d in e:
        #print d
    row.append(d)

writer.writerow(row)


#f3.write('\n')
for e in data:
    #print e
    row = []
    for d in e:
       row.append(e[d])
    
    writer.writerow(row)

f3.close()
