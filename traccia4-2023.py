p=float(input("Inserisci il prezzo degli acquisti "))
if p<50:
    vs=p*10/100
    ps=p-vs
elif p>50 and p<100:
    vs=p*20/100
    ps=p-vs
else:
    vs=p*30/100
    ps=p-vs
print("Il prezzo scontato è", ps, "Lo sconto è", vs)