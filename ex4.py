def tapis(n):
    print("+"+"-"*n+"-+") 
    for i in range(n+1):
        print("|"+"#"*(n-i),"#"*i+"|")
    print("+"+"-"*n+"-+")


tapis(10)