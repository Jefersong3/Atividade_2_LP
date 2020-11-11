''' Atividade 2 Exercicio 5 - LP  '''

def reverse_sentence2(a: str):
  sentence_list = a.split(' ')
  for i in range(len(sentence_list)):
    sentence_list[i] = sentence_list[i][::-1]

  return ' '.join(sentence_list)