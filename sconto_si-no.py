IVA=int(input("Immetti percentuale iva "))
ip1=float(input("Immetti un valore "))
ip2=float(input("Immetti un valore "))
ip3=float(input("Immetti un valore "))
S=input("Vuoi applicare sconto? (Y/n) ")
Im=float(ip1+ip2+ip3)+((ip1+ip2+ip3)*IVA/100)
if S=="Y":
    Ims=Im-(Im*65/100)
    print(Ims, Im)
else: 
    print(Im)