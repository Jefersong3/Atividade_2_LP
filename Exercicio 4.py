''' Atividade 2 Exercicio 4 - LP  '''


def is_prime(a: int):
    if not a > 1:
        return False

    divisibles = []
    for i in range(1, 100):
        if (a / i).is_integer():
            divisibles.append(i)

    if len(divisibles) > 2:
        return False
    else:
        return True