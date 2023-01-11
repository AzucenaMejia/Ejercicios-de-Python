a="hola soy johan";
print(a)
#programa que muestre por pantalla un hola mundo
print("¡Hola Mundo!")
##Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre= input("¿cómo te llamas?: ")
print("Hola",nombre)
###Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((3+2)/(2*5))**2
x=((3+2)/(2*5))**2
print("el resultado es: ",x)
####Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas=int(input("horas trabajadas: "))
precio=int(input("precio de cada hora: "))
total=precio* horas
print("El total de lo ganado es: $", total)