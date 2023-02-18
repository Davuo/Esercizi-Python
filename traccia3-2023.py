vmc=int(input("Inserisci la velocità massima consentita "))
vr=int(input("Inserisci la velocità rilevata "))
d=vr-vmc
if d>60:
    m="Limite superato, multa di 500 euro"
elif d>40:
    m="Limite superato, multa 370 euro"
elif d>10:
    m="Limite superato, multa 148 euro"
elif d<=0:
    m="Limite rispettato"
else:
    m="Limite superato, multa 36 euro"
print(m)