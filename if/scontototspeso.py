tot_s=float(input("Inserisci il totale speso "))
if tot_s>300:
    i1=tot_s-300
    vs2=i1*20/100
    i1=i1-vs2
    vs=30
    i=270
else:
    vs=tot_s*10/100
    i=tot_s-vs
    i1=0
    vs2=0
t=i1+i
vst=vs+vs2
print(t,vst)