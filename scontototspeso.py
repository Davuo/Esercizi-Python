tot_s=float(input("Inserisci il totale speso "))
if tot_s>300:
    d=tot_s-300
    vs2=d*20/100
    i1=d-vs2
    vs=300*10/100
    i=300-vs
else:
    pass
if tot_s<=300:
    vs=tot_s*10/100
    i=tot_s-vs
    i1=0
    vs2=0
t=i1+i
print(t,vs,vs2)