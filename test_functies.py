""""def willekeurige.getallen(aantal.getallen,begin,eind):
getallen = []
for i in range(0,aantal_getallen):
    if(begin < eind):
        getallen.append(r.randint(begin,eind))
    else:
        getallen.append(r.randint(eind))
"""

""""def toon_resultaat(score,max):
    if score > max:
        print(Fore.RED+
    
    procent = score/max)*100
    if procent > 80:
        print(Fore.GREEN+str(procent))
    elif procent >50 and procent < 80:
        print(Fore.RESET+str(procent))
    else:"
"""

def oppervlakte_muren():
    lijst_opp = []
    aantal_muren = int(input("geef het aantal muren in"))
    for i in range(0,aantal_muren):
        b = int(input("geef de basis in"))
        h = int(input("geef de hoogte in"))
        lijst_opp.append(b*h)
    return lijst_opp
muren = oppervlakte_muren()
print(muren)
