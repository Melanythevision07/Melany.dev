#solicitar datos al usuario
Nombre = input("¿Cuál es tu nombre?")
Año_nacimiento=int(input("¿En qué año naciste?"))

#calcuar edad (año actual aprox = 2025)
año_actual = 2025
edad = año_actual - Año_nacimiento

#verificar mayoria de edad
es_mayor = edad >= 18

#mostrar resultados por consola
print(f"Hola {Nombre},tienes aproximadamente {edad} años.")

if es_mayor:
    print("Eres mayor de edad.")
else:
     es_mayor("Eres menor de edad.")