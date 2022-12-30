e1=int(input("Inserisci l'età della prima persona "))
e2=int(input("Inserisci l'età della seconda persona "))
e3=int(input("Inserisci l'età della terza persona "))
nb=int(input("Inserisci il numero bottiglie "))
pb=float(input("Inserisci il prezzo delle bottiglie "))

if e1>=18:
    V=input("La suddetta persona è vegana? S/N ")
    if V=="S":
        c1=30+10
    else:
        c1=30
elif e1>=5:
    c1=20
else:
    c1=10
if e2>=18:
    V=input("La suddetta persona è vegana? S/N ")
    if V=="S":
        c2=30+10
    else:
        c2=30
elif e2>=5:
    c2=20
else:
    c2=10
if e3>=18:
    V=input("La suddetta persona è vegana? S/N ")
    if V=="S":
        c3=30+10
    else:
        c3=30
elif e3>=5:
    c3=20
else:
    c3=10
cc=nb*pb
if e1>=18:
    cp1=c1+100
else:
    cp1=c1
if e2>=18:
    cp2=c2+100
else:
    cp2=c2
if e3>=18:
    cp3=c3+100
else:
    cp3=c3
cp=cp1+cp2+cp3
B=input("É richiesto il babysitting? S/N ")
if B=="S":
    cp=cp+20
GP=input("Sono richiesti i giochi pirotecnici? S/N ")
if GP=="S":
    cp=cp+10
if (e1 and e2 and e3)<18:
    cc=0
cct=cp+cc
print(cct)