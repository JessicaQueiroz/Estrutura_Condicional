nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')