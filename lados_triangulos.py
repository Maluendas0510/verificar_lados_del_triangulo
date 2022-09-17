# Verificar si dados 3 numeros se pueden formar los lados de in triangulo

print("------triangulo-----")
print("--------------------")

#intput
a=int(input("dijte el valor del lado a:"))
b=int(input("diite el valor del lado b:"))
c=int(input("dijite el valor del lado c:"))

#processing
if(a+b>c) and (c+a>b) and (b+c>a):
    print("si es un triangulo")
else:
    print("no es un triangulo")
