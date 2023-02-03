#codigo de practica 1
print("hola mundo")
a=1;
b=2;
mensaje="hola a mi"
c=a+b;
print(c)
print(mensaje)
print ("la suma de a+b es : ", c)
mensaje =True
print (f"la suma de {a}+{b} es igual a {c} ")

#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:  suma= n(n+1)/2
n=int(input("ingresa un entero positivo: "))
suma=n*(n+1)/2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))