a = input('Digite algo: ')
print('É um número?', a.isnumeric())
print('É alfabético', a.isalpha())
print('É alfanumérico', a.isalnum())
print('Está em maiscúla?', a.isupper())
print('Está em minúscula?', a.islower())
print('Etá capitalizado', a.istitle())
print('Qual tipo primitivo', type(a))
print('Só tem espaços?', a.isspace())