fName = "1616484847 CDR_GRID_12-02-2019T14_09_49.csv"
fName = "1823190403 CDR_GRID_12-02-2019T14_12_36.csv"
fob = open(fName, 'rb')
x = fob.read().split(b'\n')
fob.close()
y = []
intro='''Table Head<br>['start', 'providerName', 'APartyOriginal', 'AParty', 'BPartyOriginal',
'BParty', 'duration', 'usageType', 'networkType', 'lacStartA', 'ciStartA',
'imei', 'imsia', 'address\r']<br>\n'''
p = 0
for i in x[:-1]:
    tmp = i.decode('utf-8').split(',')
    jmp = tmp[:13]
    jmp.append(str(tmp[13:]).replace('[', '').replace(']', '').replace('"', '').replace("'", ''))
    y.append(jmp)
    p = p + 1

fob = open(fName+'.html', 'w')
fob.write(intro)
fob.write('Total row count: %i<br>' % p)
fob.write('<style>\ntable, th, td {border: 1px solid black;}\n</style>\n<table>\n<tr>')
fob.write('<td>start</td><td>pNam</td><td>APartyOriginal</td><td>AParty</td><td>BPartyOriginal</td><td>BParty</td><td>dur</td><td>UsgT</td><td>NT</td><td>lacStartA</td><td>ciStartA</td><td>imei</td><td>imsia</td><td>address</td></tr>\n<tr>')
p = 0
for i in y:
    if'88' in i[5]:
        for j in i:
            fob.write('<td>'+j+'</td>')
        fob.write('</tr>\n')
        p = p + 1

fob.write('Total useful row: %i' % p)
fob.close()
