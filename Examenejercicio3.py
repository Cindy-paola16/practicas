def contar_vocales(x):
    contador=0
    total=0
    for letra in c:
        if 'a' in c:
            contador=+1
        if 'e' in c:
            contador=+1
        if 'i' in c:
            contador=+1
        if 'o' in c:
            contador=+1
        if 'u' in c:
            contador=+1
            total=contador
    return total

c=str('mi cadena')
print contar_vocales(c)