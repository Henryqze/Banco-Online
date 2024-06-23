from time import sleep


def linha():
    linha1 = '~' * 30
    print(colored_text(linha1, 'cyan'))


def inicio():
    linha()
    print(colored_text('BANCO ONLINE'.center(30), 'cyan'))
    linha()
    return inicio



def colored_text(text, color):
    colors = {
            'reset': '\033[0m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bold': '\033[1m',
            'underline': '\033[4m'
        }
    return f"{colors[color]}{text}{colors['reset']}"


def Menu():
    print(colored_text('''       MENU DO CAIXA
        [1] Sacar
        [2] Depositar
        [3] Empréstimo 
''', 'cyan'))
    

def entrada():
        while True:
            print('Seu login devera ter 8 números')
            fazerlogin = input('Digite um login: ')
            qnt_login = len(fazerlogin)
            if qnt_login < 8 or not fazerlogin.isdigit():
                print('Login invalido, o login deve conter 8 números')
                continue
            print('Login criado com sucesso')
            break
            
        sleep(1.5)

        while True:
            print('Sua senha deve conter 8 números')
            fazersenha = input('Digite uma senha: ')
            qnt_senha = len(fazersenha)
            if qnt_senha < 8 or not fazersenha.isdigit():
                print('Senha invalida, a senha deve conter 8 números')
                continue
            print('Obrigado por criar sua conta.')
            break
        
