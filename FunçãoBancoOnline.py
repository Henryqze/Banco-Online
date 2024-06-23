def linha():
    linha1 = '~' * 30
    print(colored_text(linha1, 'red'))


def inicio():
    linha()
    print(colored_text('BANCO ONLINE'.center(30), 'red'))
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
''', 'red'))