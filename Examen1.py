from mailbox import NoSuchMailboxError


mensaje = "Hola"
mensaje += " "
mensaje = "pablo"
print(mensaje)
print("concatenacion:")
mensaje = "Hola"
espacio = "  "
nombre = "pablo"              
print(mensaje + espacio + nombre)
numero_1 = 4
numero_2 = 6
resultado = numero_1 + numero_2
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)
print("Busqueda:")
mensaje = "Hola pablo"
buscar_subcadena = mensaje.frind("pablo")
print(buscar_subcadena)
print("Extraccion")
mensaje = "Hola pablo"
extraer_cadena = mensaje [1:6]
print(extraer_cadena)
