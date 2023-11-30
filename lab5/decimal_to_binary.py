

def decimal_to_function(dec):
    x=""
    while dec !=1:
        x = x+ str(dec%2)
        dec= dec/2
    x+= 1

    return int(x)


print(decimal_to_function(10))
