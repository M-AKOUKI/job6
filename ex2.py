def draw_rectangle(width,height):
    print("-"*width)
    print("|","-"*width,"|")
    for i in range(height):
        print("|"," "*width,"|")
    print("|","-"*width,"|")

draw_rectangle(15,7)