''' Atividade 2 Exercicio 1 - LP  '''

days = int(input('Digite a quantidade de dias: '))

years = days // 365
days = days % 365
months = days // 30
days = days % 30
print(f'{years} anos, {months} meses e {days} dias')