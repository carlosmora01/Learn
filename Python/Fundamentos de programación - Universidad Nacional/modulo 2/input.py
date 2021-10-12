p = float(input('Ingrese el valor en pulgadas: '))
c = 2.54*p 

print('El valor en centimetros es: ', c)

#reglas para declarar variables:

# Debe iniciar con una letra:
# Puede contener números y el carácter _
# No se puede usar nombres reservados del lenguaje
# Sensible a mayúscula y minúscula

#Como recomendación se sugiere usar nombre mnemotécnicos

segundos = int(input())

horas = int(segundos/3600)
minutos = int((segundos%3600)/60)
segundosFinal = ((segundos%3600) - minutos * 60)

print(horas,minutos,segundosFinal,sep=":")