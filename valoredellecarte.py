s1=input("s 1 ")
v1=input("v 1 ")

s2=input("s 2 ")
v2=input("v 2 ")

valori = {'k': 13,'q':12,'j':11,'10':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'1':1}
semi = {'c':4,'q':3,'f':2,'p':1}

if valori[v1] > valori[v2]:
    print('carta 1 cazzo duro',valori[v1])
elif valori[v1] < valori[v2]:
    print('carta 2 tette dure',valori[v2])
elif semi[s1] > semi[s2]:
    print('punti uguali carta 1 vince')
else:
    print('punti uguali carta 2 vince')
    