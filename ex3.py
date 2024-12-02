def triangle():
    x = int(input("Entrez une valeur"))
    i =0
    y = 0
    comp = x
    comp2 = -2
    print(" "*comp,"/\\")
    while i<x:
        comp -= 1
        comp2 += 2
        print(" "*comp,"/", " "*comp2 ,"\\")
        i += 1
        y += 1
    print("/","__"*y,"\\")

triangle()