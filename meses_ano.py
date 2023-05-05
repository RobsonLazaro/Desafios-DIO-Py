# Desafio
## Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

 
Exemplo de Entrada	
4

Exemplo de Saída:
April


month = int(input())

MESES_DO_ANO = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

if month in MESES_DO_ANO.keys():
    print(MESES_DO_ANO[month].title())
