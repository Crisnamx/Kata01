edad =int(input("Introduce tu edad:"))
if (edad >= 18):
    nombre=input("¿Como te llamas?")
    print("Bienvenid@ " + nombre + ", ¿En qué podemos ayudarte?")
else:
    print("Eres menor de edad, no podemos atenderte.")