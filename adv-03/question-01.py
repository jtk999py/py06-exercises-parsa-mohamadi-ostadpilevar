# tamrin haye adv3
'''1---> Password begriid az user, password fght dar soorati 
be taraf begid (ba moafaighiat sabt shod) ke andazash bish az 8 bashad
hatman tarkibi az adad va horof bashad
hatman tarkibi az horofe bozorg va kochak bashad'''

x = input ('enter new pssword :')

num = 0
horofb = 0
horofk = 0

for i in x:
    if i.isdigit():
        num = num+1
    if i.islower():
        horofk = horofk+1
    if i.isupper():
        horofb = horofb+1
if len(x)>8 and num>0 and horofb>0 and horofk>0:
    print('pass sabt shod')
else:
    print('pass eshtebah ast')