# afmeting muren
width_room = int(input("Geef de breedte van de kamer in: "))
height_room = int(input("Geef de hoogte"))
# geef de info van de gekozen verf in
dekking = int(input("Hoeveel m2 kun je met 1L verven?"))
lagen = int(input("Hoeveel lagen moet je voor een perfecte muur?"))
liter_pot = int(input("Hoeveel liter verf zit er in een pot?"))
#Bereken de oppervlakte van de muur.
oppervlakte = width_room * height_room
#Bepaal hoeveel verf nodig.
totale_oppervlakte = oppervlakte * 2
liter_verf = totale_oppervlakte / dekking
aantal_potten = int(liter_verf / liter_pot + 0.99)
#Schrijf het aantal benodigde potten verf,
print("Je hebt",aantal_potten,"potten verf nodig om deze muur te schilderen.")
