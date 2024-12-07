# Código Mole e Gerador de senhas
O arquivo "miniproj.py" contém os componentes que serão detalhados a seguir (Bem como um Easter egg que será mencionado no final do arquivo).
### Tela inicial:
Um simples painel de escolha para definir qual dos componentes será usado, criado usando um loop "while".
### Conversor e Tradutor de código Mole
O conversor e tradutor utiliza o dicionário "mole_code_dict" como base para conversão e tradução. A função "mole_code" é a primeira a ser chamada e determina qual tipo de tradução é necessária automaticamente, ela também detecta a presença de caracteres não encontrados na tabela de tradução e avisa o usuário sobre estes. Definido o tipo de conversão, a função chama:
A função "mole_translator", para conversões de alfabeto para Mole.
A função "mole_converter", para conversões de Mole para alfabeto.
A primeira utiliza o dicionário mencionado para encontrar o valor correspondente de cada letra e adiciona espaços conforme necessário. Retorna o texto completamente convertido.
A segunda utiliza duas listas, "Lofvalues" e "Lofkeys", que contém os valores e chaves do dicionário, respectivamente, para localizar o valor em Mole e associá-lo à sua letra correspondente. Retorna o texto completamente traduzido.
Feito isso, a função insere o texto traduzido na tela do usuário e pergunta se ele gostaria de outra tradução. A depender da resposta, a função se repete ("while" loop) ou retorna para a tela inicial.
### Gerador de senhas aleatórias
O gerador de senhas utiliza uma lista de senhas pré-fabricadas e seleciona uma delas aleatóriamente, por meio da função "Pwgen" e a lista "Pw_list". Enquanto isso ocorre, há uma pequena interação com o Deus das senhas (Responsável pela escolha). Ele lhe dirá algo importante enquanto envia sua senha para a cifra.
A função "Cesar" recebe a senha escolhida e a criptografa com uma cifra de César de 13 espaços. A função retorna a senha devidamente codificada e não modifica números e símbolos.
O Deus então mostra a senha ao usuário e pergunta a ele se gostaria de trocar. Caso positivo, a função é utilizada novamente e uma senha distinta e escolhida e codificada. Caso negativo, a função retorna.
### Easter egg
Parece que alguém mexeu no código que escrevi e mudou algumas coisas... Será que você consegue descobrir o segredo deste código??
Toda a informação que precisa será fornecida pelo código, exceto por uma (Seu trabalho descobrir qual informação falta).
A única dica que lhe dou é não reiniciar o código. Boa sorte!
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Spoilers daqui pra frente
### Easter eggs:
Aqui explicarei como as funções "Easter_eggX" funcionam.
A primeira função é onde realmente ocorre o Easter egg. Há uma senha faltando e seu trabalho é descobrir qual é, mas primeiro precisa corrigir as senhas que estão erradas. Essa função determina se a senha que você escreveu é uma versão correta ou a senha correta e age de acordo. A senha secreta só é liberada quando você conseguir descobrir as senhas que estão erradas. Senhas corrigidas: ['Language0001$','Iguana0035$','Height8849$']
A segunda função é a que fornece informações ao usuário conforme ele usa o programa, algumas estão em código mole e precisam ser traduzidas.
A terceira função oferece a lista de senhas quando o painel secreto é acessado.
