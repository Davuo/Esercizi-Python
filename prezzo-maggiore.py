gi=int(input())
ga=int(input())
m=int(input())
p=int(input()) 
Im=float(gi*5)+(ga*1)+(m*0.50)+(p*10)
if Im>30:
    Ims=Im-(Im*10/100)
    print(Ims)
else:
    print(Im)