from FunçãoBancoOnline import *
from time import sleep

def main():
    inicio()
    valoremconta = 3500
    cem = 100
    dez = 10

    entrada()
    try:
        while True:
            Menu()
            opção = input('Digite a opção: ')

            if opção == '1':
                Sacar = float(input('Qual valor que deseja sacar: '))
                if Sacar <= valoremconta:
                    valoremconta -= Sacar
                    print(f'Você sacou o total de {Sacar}. Seu saldo atual é de {valoremconta}')
                else:
                    print('Saldo insuficiente')


                resp = str(input('Deseja voltar para o menu inicial ou sair da sua conta:[Sair/voltar] ')).upper()[0]
            
            elif opção == '2':
                Depositar = float(input('Qual o valor a depositar: '))
                valoremconta += Depositar
                print(f'Você depositou {Depositar}. Seu saldo atual é de {valoremconta}')
            
            
                resp = str(input('Deseja voltar para o menu inicial ou sair da sua conta:[Sair/voltar] ')).upper()

            elif opção == '3':
                Empréstimo = float(input('Qual o valor que deseja pedir de empréstimo:  '))
                aprovado = (valoremconta * dez) / cem
                print(F'O valor de empréstimo aprovado foi {aprovado}')

                Scp = str(input('Deseja aceitar o valor aprovado:[S/N] ')).upper()[0]
                if Scp in 'Ss':
                    valoremconta += aprovado
                    print(f'O seu saldo atual é de {valoremconta}')
                if Scp in 'Nn':
                    print(F'Entendo.')
            
            else:
                print('opção invalida!')

                resp = input('Deseja voltar para o menu inicial ou sair da sua conta:[Sair/voltar] ').upper()[0]
                if resp == 'SAIR':
                    break
                elif resp == 'VOLTAR':
                    print('voltando...')
                else:
                    print('Por favor, digite somente sair ou voltar')

            if resp in 'S':
                print(f'O seu Saldo atual é de {valoremconta}')
                break
    except:
        print('Erro nos dados!')
    print("Banco Online agradece a confiança.")

if __name__ == "__main__":
    main()