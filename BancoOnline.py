from FunçãoBancoOnline import *
from time import sleep


cem = 100
dez = 10

inicio()
def main():
    valoremconta = 3500

    try:
        while True:
            jácadastrado = input('Você já é castrado:[Sim/Não] ').upper()[0]
            if jácadastrado in 'S':
                break
            elif jácadastrado in 'N':
                entrada()
            else:
                print('Coloque somente somente [Sim] ou [Não]')

        while True:               
            Menu()
            opção = input('Digite a opção: ')
            if opção == '1':
                Sacar = float(input('Qual valor que deseja sacar: '))
                if Sacar <= valoremconta:
                    valoremconta -= Sacar
                    print(f'Você sacou o total de {Sacar:.2f}. Seu saldo atual é de {valoremconta:.2f}')
                else:
                    print('Saldo insuficiente')

                
            elif opção == '2':
                Depositar = float(input('Qual o valor a depositar: '))
                valoremconta += Depositar
                print(f'Você depositou {Depositar:.2f}. Seu saldo atual é de {valoremconta:.2f}')
            

            elif opção == '3':
                Empréstimo = float(input('Qual o valor que deseja pedir de empréstimo:  '))
                aprovado = (valoremconta * dez) / cem
                print(F'O valor de empréstimo aprovado foi {aprovado:.2f}')

                Scp = str(input('Deseja aceitar o valor aprovado:[S/N] ')).upper()[0]
                if Scp in 'Ss':
                    valoremconta += aprovado
                    print(f'O seu saldo atual é de {valoremconta:.2f}')
                if Scp in 'Nn':
                    print(F'Entendo.')

            else:
                print('opção invalida!')

            while True:
                resp = input('Deseja voltar para o menu inicial ou sair da sua conta:[Sair/voltar] ').upper()[0]
                if resp == 'S':
                    print(f'O seu Saldo atual é de {valoremconta:.2f}')
                    print("Banco Online agradece a confiança.")
                    return
                elif resp == 'V':
                    print('voltando...')
                    break
                else:
                    print('Por favor, digite somente sair ou voltar')
    except:
        print('Erro nos dados!')        

if __name__ == "__main__":
    main()