e=int(input("Inserisci l'età della persona "))
if e>=75:
    m="Sei un esponente della generazione silenziosa"
elif e<=74 and e>=57:
    m="Sei un BabyBoomer"
elif e>40:
    m="Sei un Gen X"
else:
    m="Sei un Millennial"
print(m)