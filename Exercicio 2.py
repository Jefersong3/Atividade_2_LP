''' Atividade 2 Exercicio 2 - LP  '''

import math

a = int(input('Informe o valor de A: '))

b = int(input('Informe o valor de B: '))

c = int(input('Informe o valor de C: '))

triangle = True

if a < b:
  if b < c:
    print(a);
    print(b);
    print(c);
    triangle = not (a + b < c);
  else:
    if a < c:
      print(a);
      print(c);
      print(b);
      triangle = not (a + c < b);
    else:
      print(c);
      print(a);
      print(b);
      triangle = not (c + a < b);
else:
  if b < c:
    if a < c:
      print(b);
      print(a);
      print(c);
      triangle = not (b + a < c);
    else:
      print(b);
      print(c);
      print(a);
      triangle = not (b + c < a);
  else:
    print(c);
    print(b);
    print(a);
    triangle = not (c + b < a);

if triangle:
  perimeter = (a + b + c) / 2;
  area = math.sqrt(perimeter * ((perimeter - a) + (perimeter - b) +(perimeter - c)))
  print('A area do triangulo e: ', area)
else:
  print('Os valores informados nao formam um triangulo.')