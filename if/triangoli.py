l1=int(input("Inserisci il valore del lato 1 "))
l2=int(input("Inserisci il valore del lato 2 "))
l3=int(input("Inserisci il valore del lato 3 "))
if l1>=(l2+l3) or l2>=(l1+l3) or l3>=(l1+l2):
    t="nulla"
elif l1!=l2!=l3:
    t="scaleno"
elif l1==l2!=l3 or l2==l3!=l1 or l1==l3!=l2:
    t="isoscele"
elif l1==l2==l3:
    t="equilatero"
print(t)
