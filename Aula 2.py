a=int(input('Digite o valor 1:'))
b=int(input('Digite o valor 2:'))
soma = a+b
subtracao = a-b
multiplicacao= a*b
divisao=a/b
resto= a % b
print('soma: {soma}. \nsubtracao: {subtracao}. '
'\nmultiplicacao: {multiplicacao}'
'\ndivisao: {divisao}'
 '\nresto: {resto}'.format(soma=soma,
                          subtracao=subtracao,
                          resto=resto,
                          multiplicacao=multiplicacao,
                          divisao=divisao))
