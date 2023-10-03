'''Crear un analizador de exto.
1.- pedir al usiario que ingrrese un txt************
2.- ingrese 3 letras a su eleccion***********
3.- al tener esos datos, nuestro programa hara 5 analisis
    -devolver cuantas veces aparece cada una de las letras que eligio **********
    -cuantas palabras hay a lo largo de todo el texto*************
    -informar cual es la primera y ultima letra del texto********
    -invertir el orden de las palabras 
    -si la palabra "Python" se encuentra en el texto
'''


text = input('Ingresa un Texto\n').lower()
print('Ingresa 3 letras')
letras = []
letra1 = input('Letra 1:\n').lower()
letras.append(letra1)
letra2 = input('Letra 2:\n').lower()
letras.append(letra2)
letra3 = input('Letra 3:\n').lower()
letras.append(letra3)
text_split = text.split()

print('-'*70)
print(f'''La letra "{letras[0]}" aparece {text.count(letras[0])} veces en tu Texto''')
print('-'*70)
print(f'''La letra "{letras[1]}" aparece {text.count(letras[1])} veces en tu Texto''')
print('-'*70)
print(f'''La letra "{letras[2]}" aparece {text.count(letras[2])} veces en tu Texto''')
print('-'*70)
print(f'''Tu texto tiene {len(text_split)} palabras''')
print('-'*70)
print(f'''La primer letra de tu texto es "{text[0]}"''')
print('-'*70)
print(f'''La primer palabra de tu texto es "{text_split[0]}"''')
print('-'*70)
print(f'''La Ultima letra de tu texto es "{text[-2]}"''')
print('-'*70)
print(f'''La ultima palabra de tu texto es "{text_split[-1]}"''')
print('-'*70)
text_split.reverse()
text_invertido = ' '.join(text_split)
print(f'''Asi se ve tu texto con el orden de las palabras invertido:
{text_invertido}''')

buscar = 'Python' in text
dic = {True:'sí', False: 'no'}
print(f'''La palabra python {dic[buscar]} esta en el poema''')


