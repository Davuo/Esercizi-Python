#Dati i dipendenti di un azienda calcolare e visualizzare la retribuzione media dei dipendenti maschi 
#e delle dipendenti donne 
#e la retribuzione media dei dipendenti con più di 10 anni di servizio
#st=stipendio; se=sesso; p10=persone con più di 10 anni di servizio ans=anni di servizio m=dipendenti maschi(contatore);
#f=dipendenti femmine(contatore); d10=dipendenti con più di 10 anni di servizio(contatore);
#sm=stipendio maschi(accumulatore); sf=stipendio femmine(accumulatore); 
#sd10=stipendio dipendenti con più di 10 anni di servizio(accumulatore)
#msm=media stipendi maschi; msf=media stipendi femmine; msd10=media stipendi dipendenti con più di 10 anni di servizio#
m=0
f=0
d10=0
sm=0
sf=0
sd10=0
st=float(input("Inserisci lo stipendio del dipendente "))
while st>0:
    s=str(input("Inserisci il sesso del dipendente M/F "))
    if s=="M":
        sm=sm+st
        m=m+1
    else:
        sf=sf+st
        f=f+1
    ans=int(input("Inserisci gli anni di servizio "))
    if ans>10:
        sd10=sd10+st
        d10=d10+1
    else:
        pass
    st=float(input("Inserisci lo stipendio del dipendente "))
else:
    msm=sm/m
    msf=sf/f
    msd10=sd10/d10
    print("Lo stipendio medio dei maschi è ",msm)
    print("Lo stipendio medio delle femmine è ",msf)
    print("Lo stipendio medio dei dipendenti con più di 10 anni di servizio è ",msd10)