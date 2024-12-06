from time import sleep
from random import randint
mole_code_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
       'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
        'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....','7': '--...', '8': '---..', '9': '----.', ' ': '/', '/': ' '}
Lofvalues = list(mole_code_dict.values())
Lofkeys = list(mole_code_dict.keys())
starttext = '''Conversor e Tradutor de Código Mole
Para utilizar, insira o texto em linguagem tradicional ou siga o modelo abaixo para Código Mole:
Exemplo: .- -... -.-./.- -... -.-.
Tradução: abc abc
Utilize espaços para diferenciar letras e barras para diferenciar palavras'''
def mole_translator(text: str) -> str: # De alfabeto para mole
    global mole_code_dict
    new_text = ''
    text = text.split(' ')
    for ind in range(len(text)):
        word = text[ind]
        for i in word:
                for j in i:
                    new_text += mole_code_dict[j] + ' '
        if ind != len(text)-1:
            new_text += '/'
    return new_text.strip()

def mole_converter(text: str) -> str: # De mole para alfabeto
    global mole_code_dict, Lofvalues, Lofkeys
    new_text = ''
    for word in text.split('/'):
        for s in word.split():
            if s in Lofvalues:
                new_text += Lofkeys[Lofvalues.index(s)]
        new_text += ' '
    return new_text.strip()
def mole_code() -> None: # Função que converte e traduz código Mole
    global mole_code_dict, Lofvalues, Lofkeys, starttext, Ndt
    print(starttext)
    while True:
        CNF = [] # Caracteres não encontrados
        print('Por favor insira o texto a ser traduzido:')
        texto = input().strip()
        T = False
        M = False
        if texto != '':
            Ndt += 1
            EE = Easter_egg(texto)
            EE2 = Easter_egg2()
            if EE == 1:
                continue
            elif EE == 2:
                raise BrokenPipeError('Este programa cumpriu sua função')
            texto = texto.lower()
            for i in texto:
                if i in Lofkeys and i not in [' ', '/']:
                    T = True       
                elif i in ['.', '-', '/']:
                    M = True
                elif not i.isspace():
                    CNF.append(i)
        if T and M:
            print('Por favor use somente uma linguagem e tente novamente')
        elif CNF:
            print(f'Os seguintes caracteres não podem ser traduzidos: {CNF}')
            print('Por favor retire-os e tente novamente')
        else:
            if T:
                print('Texto traduzido:', mole_translator(texto))
            else:
                print('Texto traduzido:', mole_converter(texto))
        
        print('Caso deseje realizar mais uma tradução, pressione Enter. Caso contrário, responda com N.')
        answer = input()
        if answer.lower() == 'n':
            print('Obrigado por usar o Conversor e Tradutor de Código Mole!')
            break
    return
#Height, Iguana Language
if True: #NÃO ABRIR, ARMAZÉM DE SENHAS
    Ndt = 0
    Pw_list = ['Alfa0001!', 'Bismarck1730@', 'Corretor7768#', 'Destruidor1190%', 'ValueNotFound', 'Formacao1357*', 'Garfield9999?', 'Height7736$', 'Iguana1910$', 'Judith1773/', 'Komodo4949!', 'Sprache0001', 'Monumento4479/','Number1212*', 'Observatório1333&', 'Password0720?', 'Quilha0707!', 'Retaguarda8172#', 'Synonym9976!', 'Tucano9876.', 'Ultravioleta5701;', 'Valorizacao0076.','Wellington0000!', 'Xafarizcomx1019@', 'Yupiiiyy1111;', 'Zebracolorida9191#']
def Cesar(Pw: str) -> str: #Realiza a cifra de Ceasar em uma string
    Alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    N_pw = ''
    for i in Pw.lower():
        if i in Alfabeto:
            ind = Alfabeto.index(i)
            ind = ind + 13
            if ind > 25:
                ind = ind - 26
            N_pw += Alfabeto[ind]
        else:
            N_pw += i
    return N_pw

def Pwgen() -> None: # Printa a senha escolhida pelo Deus na tela
    global Pw_list, Ndt, Phrases_list
    EE2 = Easter_egg2()
    if EE2 == 1:
        return
    print('O Deus das senhas fará sua escolha...')
    while True:
        chosen_n = randint(0, len(Pw_list)-1)
        Pw_chosen = Pw_list.pop(chosen_n)
        sleep(3)
        if chosen_n != 4:
            Pw_chosen = Cesar(Pw_chosen)
        else:
            print('Estranho, nunca tinha acontecido isso antes...')
            sleep(1)
            print('Oh...')
            sleep(2)
            raise BrokenPipeError('A senha parece ter sido removida a força por alguém...')
        print(Phrases_list[randint(0, len(Phrases_list)-1)])
        print('')
        print(Pw_chosen.capitalize())
        print('O que acha? (S/N)')
        Ndt += 1
        resp = input().lower()
        if resp =='s':
            print('Sucesso!!! O humano gostou da minha senha')
            sleep(2)
            break
        elif resp == 'n':
            print('Okay, vamos tentar de novo...')
        else:
            print('Ei, humano!')
            print('Eu te fiz uma pergunta')
    return


def Easter_egg(A) -> int: #NÃO ABRA SE QUISER DESCOBRIR O EASTER EGG
    global LofcorrectedP
    secretP = 'Espeon_shiny0196$'
    if A == secretP:
        print('Ok, ok, ok, ok, ok, ok, ok, ok, ok')
        sleep(3)
        print('Você descobriu...')
        sleep(5)
        print('Toma, o Easter Egg é seu')
        sleep(4)
        print('''https://youtu.be/dQw4w9WgXcQ?si=pM__pJ5kfFkhehj7''')
        sleep(3)
        print('É tudo que eu estava escondendo, pega logo')
        return 2
    elif A in LofcorrectedP and LofcorrectedP != []:
        ind = LofcorrectedP.index(A)
        LofcorrectedP.pop(ind)
        print(f'Faltam {len(LofcorrectedP)}...')
        return 1
    if LofcorrectedP == []:
        sleep(3)
        print('Você me pegou...')
        print(secretP)
        LofcorrectedP.append('################################')
    else:
        return 0
def Easter_egg2() -> None: #NÃO ABRA SE QUISER DESCOBRIR O EASTER EGG
    global Ndt
    if Ndt == 3:
        print('Alguém está aí?')
    elif Ndt == 5:
        print('... --- ...')
    elif Ndt == 7:
        print('Sim, alguém usando o programa')
        print('Tem um ... . --. .-. . -.. --- nele, tente -.. . ... -.-. --- -... .-. .. .-.')
    elif Ndt == 9:
        print('Olhe as ... . -. .... .- ... que estão disponíveis, deve ajudar a descobrir o que há de errado')
        print('Digite ----. --... no painel de escolha, você deve conseguir abrir um @*!¨& #@(*!$%')
def Ester_egg3(): #NÃO ABRA SE QUISER DESCOBRIR O EASTER EGG
    global Pw_list
    print('Admin code detected')
    print(Pw_list)
    print('Você conseguiu...')
    print('Deve haver algum tipo de código para identificar as senhas que estão erradas... Eu sei que são 3')
    print('Estranho, uma das senhas está faltando... Ela deve ser utilizada para alguma coisa')
if True: #NÃO ABRA SE QUISER DESCOBRIR O EASTER EGG
    LofcorrectedP = ['Language0001$','Iguana0035$','Height8849$']
    Phrases_list = ['Você sabia que existem 35 espécies de Iguana?','Aguardando, aguardando, aguardando...', '*Inserir música de elevador aqui*','Um elefante incomoda muita gente, dois elefantes incomodam muito mais...', 'Você sabia que o Everest tem 8849 metros de altura?','Muitas vezes prestamos tanta atenção nos cifrões que esquecemos de olhar o que está próximo deles...','A vida é muito importante para ser levada a sério.', 'O importante não é vencer todos os dias, mas lutar sempre.','Você sabia que o Inglês é considerado a língua número 1?', 'Escolher o seu tempo é ganhar tempo.']
if __name__ == '__main__':
    print('''Escolha o programa que deseja utilizar:
1 - Conversor e Tradutor de código Mole
2 - Gerador de senhas aleatórias
3 - Sair''')
    while True:
        Pw_list = ['Alfa0001!', 'Bismarck1730@', 'Corretor7768#', 'Destruidor1190%', 'ValueNotFound', 'Formacao1357*', 'Garfield9999?', 'Height8849$', 'Iguana0035$', 'Judith1773/', 'Komodo4949!', 'Sprache0001', 'Monumento4479/','Number1212*', 'Observatório1333&', 'Password0720?', 'Quilha0707!', 'Retaguarda8172#', 'Synonym9976!', 'Tucano9876.', 'Ultravioleta5701;', 'Valorizacao0076.','Wellington0000!', 'Xafarizcomx1019@', 'Yupiiiyy1111;', 'Zebracolorida9191#']
        print('')
        imp = int(input('Por favor escolha uma opção:'))
        if imp == 1:
            print('')
            mole_code()
            print('''
Escolha o programa que deseja utilizar:
1 - Conversor e Tradutor de código Mole
2 - Gerador de senhas aleatórias
3 - Sair''')
        elif imp == 2:
            print('')
            Pwgen()
            print('''
Escolha o programa que deseja utilizar:
1 - Conversor e Tradutor de código Mole
2 - Gerador de senhas aleatórias
3 - Sair''')
        elif imp == 3:
            print('Obrigado por utilizar os programas!')
            break
        elif imp == 97:
            Ester_egg3()
        else:
            print('Opção inválida!')