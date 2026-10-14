a = int(input("Brutopalk: ")) 
sotsiaalmaks = (33*a)/100
töötuskindlustusmakse_1 = (1.6*a)/100
kogumispension = (2*a)/100
töötuskindlustusmakse_2 = (0.8*a)/100

with open("palgaraport_Maria_Sibolt.txt", "w") as fail:
    fail.write("Töötaja palk ja maksud\n")
    fail.write("                       \n")
    fail.write("Brutopalk: " + str(a) + " eurot\n")
    fail.write("Töötuskindlustusmakse: " + str(töötuskindlustusmakse_1) + " eurot\n")
    fail.write("Kogumispension: " + str(kogumispension) + " eurot\n")
    
    if a*12 <= 14400:
        tulumaks_min = 654
    elif a*12 > 14400 and a*12 <= 25200:
        tulumaks_min = 654 - (654*(a - 1200))/900
    else:
        tulumaks_min = 0

    fail.write("Arvestatud tulumaksuvaba miinimum on " + str(tulumaks_min) + " eurot\n")
    
    tulumaks = (a - töötuskindlustusmakse_1 - kogumispension - tulumaks_min)*0.2
    if tulumaks < 0:
        tulumaks = 0
    netopalk = a - töötuskindlustusmakse_1 - kogumispension - tulumaks

    fail.write("Tulumaks: " + str(tulumaks) + " eurot\n")
    fail.write("Netopalk: " + str(netopalk) + " eurot\n")
    
    fail.write("                       \n")
    fail.write("                       \n")
   
    fail.write("Tööandja kulud ja maksud\n")
    fail.write("                       \n")
    fail.write("Brutopalk: " + str(a) + " eurot\n")
    fail.write("Sotsiaalmaks: " + str(sotsiaalmaks) + " eurot\n")
    fail.write("Töötuskindlustus: " + str(töötuskindlustusmakse_2) + " eurot\n")
    
    kogukulu = a + sotsiaalmaks + töötuskindlustusmakse_2
    fail.write("Kogukulu tööandjale: " + str(kogukulu) + " eurot\n")

print("Palgaraport on failis: palgaraport_Maria_Sibolt.txt")
