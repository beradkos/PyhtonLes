def xtekensvan(aantal,tekst):
    print(tekst[0:aantal])

xtekensvan(3,"Hallloooe")
tekst = "Dit is een tekst"
for i in range(1,len(tekst)+1):
    xtekensvan(i,tekst)