class persona:
    def __init__(self,nome,cognome,annodinascita,altezza,peso,sesso):
        self.nome = nome
        self.cognome = cognome
        self.annodinascita = annodinascita
        self.altezza = altezza
        self.peso = peso
        self.sesso = sesso

persone = []
pg=2023
npg = ""
cpg = ""
sesso = ""
conta_altp = 0
conta_pp = 0
checkNascita = False
checkAltezza = False
checkPeso = False

for i in range(50):
    checkNascita = False 
    checkAltezza = False
    checkPeso = False 
    print(i,")")
    nome=input("Inserisci il nome ")
    cognome=input("inserisci il cognome ")
    while checkNascita == False:
        annodinascita=int(input("Inserisci l'anno di nascita "))
        if (annodinascita >= 1900) and (annodinascita <= 2022):
            checkNascita = True

    while checkAltezza == False:
        altezza=float(input("Inserisci l'altezza in centimetri "))
        if (altezza >= 50) and (altezza <= 230):
            checkAltezza = True
    
    while checkPeso == False:
        peso=float(input("Inserisci il peso in kg "))
        if (peso >= 10) and (peso <= 150):
            checkPeso = True
    sesso=input("M/F/A ")
    persone.append(persona(nome, cognome, annodinascita, altezza, peso, sesso))

for i in range(50):
    if persone[i].annodinascita < pg:
        npg = persone[i].nome
        cpg = persone[i].cognome
        sesso = persone[i].sesso
    if persone[i].altezza >= 200:
        conta_altp+=1
    if persone[i].peso >= 100:
        conta_pp+=1


print("Le persone con altezza maggiore di 200 cm sono",conta_altp, "e più pesanti di 100kg sono", conta_pp )

print(cpg,npg, "è la persona più giovane ed è di sesso", sesso)

