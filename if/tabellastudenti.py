class studente:
    def __init__ (self,nome,cognome,indirizzo,annodinascita,telefono):
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo
        self.annodinascita = annodinascita
        self.telefono = telefono

studenti = []

for i in range(3):
    print(i,")")
    nome=input("Inserisci il nome dello studente ")
    cognome=input("Inserisci il cognome dello studente ")
    indirizzo=input("Inserisci l'indirizzo dello studente ")
    annodinascita=int(input("Inserisci l'anno di nascita dello studente "))
    telefono=int(input("Inserisci il numero di telefono "))
    studenti.append(studente(nome, cognome, indirizzo, annodinascita, telefono))

for i in range(3):
    print((i+1),")","( Cella della lista numero",i,") ")
    print("Nome:",studenti[i].nome)
    print("Cognome:",studenti[i].cognome)
    print("Indirizzo:",studenti[i].indirizzo)
    print("Anno di nascita:",studenti[i].annodinascita)
    print("Telefono:",studenti[i].telefono)