import csv
import random

#Vecht functie
def vecht(level,pad,check,behendigheid,kracht):

    #Totale power speler
    power = behendigheid + kracht

    #power van bosman, aardman en trol afhankelijk van het gekozen level
    bosman = 2*random.randint((level-1)*10,level*10)
    aardman = 2*random.randint((level-1)*20,level*20)
    trol = 2*random.randint((level-1)*40,level*40)

    verdient = 0

    #Check 0 om te vluchten
    if check == 0:
        pass
    else:
        #Nested if else loop voor gevecht
        if pad == 1 :
            if power > bosman:
                verdient = power - bosman
            else:
                pass
        elif pad == 2:
            if power > aardman:
                verdient = power - aardman
            else:
                pass
        else:
            if power > trol:
                verdient = power - trol
            else:
                pass

    #Verdiende goudstukken
    return verdient

#Koop/verkoop functie
def koop_of_verkoop(status,voorwerp,goudstukken):

    #Prijzenlijst
    prijs = {1:50,2:60}

    #Kopen
    if status == 1:
        if goudstukken < prijs[voorwerp]:
            print "Sorry je hebt niet genoeg goudstukken"
        else:
            goudstukken = goudstukken - prijs[voorwerp]

    #Verkoop
    else:
        goudstukken = goudstukken + prijs[voorwerp]

    return goudstukken
        
        



if __name__ == '__main__':
    #Ophalen opgeslagen data
    ifile = open('Accounts.csv','r')
    reader = csv.reader(ifile)

    #Data inlezen en aanmaken dictionary voor naam en aantal goudstukken
    name_dict = {}
    for row in reader:
        name_dict[row[0]] = row[1]
    ifile.close()

    #Ingevulde naam checken met opgeslagen namen
    name = raw_input("Vul hier uw naam in: ")
    if name in name_dict.keys():
        print("U heeft eerder gespeeld")
        goudstukken = int(name_dict[name])
    else:
        goudstukken = 0

    #Vorig aantal goudstukken 
    print "U had toen " + str(goudstukken) +" goudstukken."

    #Power kracht + behendigheid
    while True: 
        try: 
            kracht = int(raw_input("\nHoe krachtig ben je kies een getal van 1 t/m 100 : "))
        except ValueError:
                print("Alleen getallen")
        if 1 <= kracht <= 100:
            break
        
        else:
            print("1 t/m 100 aub")

    while True:
        try:
            behendigheid = input("Hoe behendig ben je kies een getal van 1 t/m 100 : ")
        except ValueError:
            print("Alleen getallen")
            continue
        if 1 <= kracht <= 100:
            break
        else:
            print("1 t/m 100 aub")
        
    power = kracht + behendigheid

    #While loop status check
    status = 0
    while status != 4 :
        
        #Welk level er wordt gekozen
        verdient = 0
        level = input("\nEnter Kies 1 t/m 3 voor een level en 4 om te kopen/verkopen: ")
        if level == 4:
            break
        
        #Input voor welk pad en keuze vechten/vluchten
        pad = input("Kiest u pad 1, 2 of 3 : ")
        check = input("Kies 1 om te vechten en 2 om te vluchten : ")


        verdient = vecht(level,pad,check,behendigheid,kracht)
        goudstukken = goudstukken + verdient
        name_dict[name] = goudstukken

        #Output vecht
        print "U heeft " + str(verdient) + " goudstukken gevonden ."

    print "\nU heeft " + str(goudstukken) + " goudstukken gevonden ."

    #Kopen/verkopen
    status = 0
    gekocht = []

    #While loop voor verkopen en kopen van voorwerpen
    while status !=3:
        try:
            status = int(raw_input("\n Kies 1 om te kopen en 2 om te verkopen"))

        except ValueError:
            print("Alleen getallen aub")
            continue
        
        if 1 <= status <= 2:
            break
        
        else: 
            print("Kies 1 kopen of 2 verkopen: ")
            continue
        
    #Input wapen of schild
    while 1 <= status <=2:
        try:
            voorwerp = int(raw_input("Kies 1 voor een wapen en 2 voor een schild : "))

        except ValueError:
            print("Alleen getallen")
            continue
        
        if 1 <= voorwerp <= 2:
            break
        else:
            print("Kies 1 voor een wapen en 2 voor een schild")
            continue
        

    #Aanroepen koop_of_verkoop functie
    goudstukken = koop_of_verkoop(status,voorwerp,goudstukken)

    #Aantal goudstukken bij het einde
    print "\nItem gekocht u heeft nog " + str(goudstukken) + " goudstukken ."
        
                
    #Opslaan gegevens
    ofile = open('Accounts.csv','w')
    writer = csv.writer(ofile,lineterminator = '\n')
    for key,value in name_dict.items():
        writer.writerow([key,value])
    ofile.close()

