def chiffrage(mot):
    for i in mot:
        transform = ord(i)
        if 65<= transform <= 90 or 97 <= transform <= 122:
            print(chr(ord(i) + 3))
        else:
            print(i)
            


chiffrage("chien de garde")