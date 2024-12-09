cspr = int(input("Input the price you have bought the item for. Rs."))
spr = int(input("Input the price you have sold the item for. Rs."))
if (spr > cspr):
    prft = spr - cspr
    print("You have made a profit of Rs.", prft)
else:
    loss = cspr - spr
    print("You have made a loss of Rs.", loss)