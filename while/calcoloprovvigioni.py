cm=0
acp=0
while cm!=12:
    vt=float(input("Inserisci le vendite di tè "))
    vc=float(input("inserisci le vendite di caffè "))
    if vc>5000:
        pc=vc*10/100
    else:
        pc=vc*5/100
    if vt>10000:
        pt=vt*16/100
    else:
        pt=vt*4/100
    tot=vc+vt
    if tot>20000:
        pr=tot*12/100
    else:
        pr=0
    tp=pc+pt+pr
    acp=acp+tp
    cm=cm+1
else:
    print(acp)