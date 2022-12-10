e=int(input("Inserisci l'età della persona"))
p=float(input("Inserisci il prezzo del biglietto"))

if e<5:
    print("Entri gratis")
elif e>60:
    print("Entri gratis")
elif e<18:
    ps=p-(p*20/100)
    print("Il prezzo del biglietto scontato è", ps)