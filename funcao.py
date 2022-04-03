from selenium import webdriver
from time import sleep
import string
import unicodedata
from keyboard import read_key

dicinario_palavras = {
    'A': {
        'Cor':      'azul',
        'Nome':     'ayrton',
        'Cep':      'amazonia',
        'Famosos':  'ayrton senna',
        'Animal':   'anta',
        'Marca':    'audi',
        'Mse':      'anta',
        'Carro':    'amarok',
        'Objeto':   'apagador',
        'Pch':      'antebraco',
        'Tv':       'a fazenda',
        'Esporte':  'atletismo',
    },
    'B': {
        'Cor':      'branco',
        'Nome':     'bruno',
        'Cep':      'brasil',
        'Famosos':  'bernardo silva',
        'Animal':   'burro',
        'Marca':    'bmw',
        'Mse':      'burra',
        'Carro':    'boxer',
        'Objeto':   'borracha',
        'Pch':      'braco',
        'Tv':       'brasileirao',
        'Esporte':  'badmington',
    },
    'C': {
        'Cor':      'carmin',
        'Nome':     'carlos',
        'Cep':      'cazequistao',
        'Famosos':  'cardi b',
        'Animal':   'coelho',
        'Marca':    'c e a',
        'Mse':      'coitada',
        'Carro':    'c4',
        'Objeto':   'caneta',
        'Pch':      'cordas vocais',
        'Tv':       'caldeirao do hulk',
        'Esporte':  'canoagem',
    },
    'D': {
        'Cor':      'dourado',
        'Nome':     'daniel',
        'Cep':      'dinamarca',
        'Famosos':   'daniel alves',
        'Animal':   'dromedario',
        'Marca':    'dannete',
        'Mse':      'doida',
        'Carro':    'discovery',
        'Objeto':   'dedal',
        'Pch':      'dedo',
        'Tv':       'dance o clip',
        'Esporte':  'danca',
    },
    'E': {
        'Cor':      'esmeralda',
        'Nome':     'evandro',
        'Cep':      'eslovaquia',
        'Famosos':  'eminem',
        'Animal':   'elefante',
        'Marca':    'ebay',
        'Mse':      'exentrica',
        'Carro':    'elba',
        'Objeto':   'escaner',
        'Pch':      'esofago',
        'Tv':       'eliana',
        'Esporte':  'esgrima',
    },
    'F': {
        'Cor':      'fucsia',
        'Nome':     'fabiano',
        'Cep':      'florida',
        'Famosos':  'fabio porchat',
        'Animal':   'furao',
        'Marca':    'forever 21',
        'Mse':      'fofa',
        'Carro':    'fusion',
        'Objeto':   'furadeira',
        'Pch':      'faringe',
        'Tv':       'family guys',
        'Esporte':  'futebol',
    },
    'G': {
        'Cor':      'gelo',
        'Nome':     'glaucia',
        'Cep':      'groelandia',
        'Famosos':  'galvao',
        'Animal':   'girafa',
        'Marca':    'groove',
        'Mse':      'grossa',
        'Carro':    'gla',
        'Objeto':   'geladeira',
        'Pch':      'guela',
        'Tv':       'game of thrones',
        'Esporte':  'golf',
    },
    'H': {
        'Cor':      'hortela',
        'Nome':     'heitor',
        'Cep':      'holanda',
        'Famosos':  'haminton',
        'Animal':   'hipopotamo',
        'Marca':    'hard rock',
        'Mse':      'horrorosa',
        'Carro':    'hb2',
        'Objeto':   'harpa',
        'Pch':      'himem',
        'Tv':       'happy hour',
        'Esporte':  'handball',
    },
    'I': {
        'Cor':      'independencia',
        'Nome':     'iago',
        'Cep':      'india',
        'Famosos':  'irv gotti',
        'Animal':   'iguana',
        'Marca':    'ibm',
        'Mse':      'idolatrada',
        'Carro':    'idea',
        'Objeto':   'ima',
        'Pch':      'iris',
        'Tv':       'impossivel',
        'Esporte':  'iatismo',
    },
    'J': {
        'Cor':      'jade',
        'Nome':     'joao',
        'Cep':      'jordanesia',
        'Famosos':  'joao felix',
        'Animal':   'jumento',
        'Marca':    'jeep',
        'Mse':      'jumenta',
        'Carro':    'jetta',
        'Objeto':   'jarra',
        'Pch':      'joelhos',
        'Tv':       'jack irish',
        'Esporte':  'judo',
    },
    'L': {
        'Cor':      'lilas',
        'Nome':     'livia',
        'Cep':      'libano',
        'Famosos':  'luis soares',
        'Animal':   'lagarto',
        'Marca':    'lindoyas',
        'Mse':      'linda',
        'Carro':    'livinia',
        'Objeto':   'linha',
        'Pch':      'lingua',
        'Tv':       'la casa de papel',
        'Esporte':  'luta livre',
    },
    'M': {
        'Cor':      'marrom',
        'Nome':     'marcos',
        'Cep':      'marrocos',
        'Famosos':  'marcos goleiro',
        'Animal':   'macaco',
        'Marca':    'mm',
        'Mse':      'maravilhosa',
        'Carro':    'master',
        'Objeto':   'macaneta',
        'Pch':      'mesocardio',
        'Tv':       'mais voce',
        'Esporte':  'mma',
    },
    'N': {
        'Cor':      'neve',
        'Nome':     'nilton',
        'Cep':      'nicaragua',
        'Famosos':  'newton',
        'Animal':   'narval',
        'Marca':    'nivea',
        'Mse':      'noia',
        'Carro':    'nimbus',
        'Objeto':   'navalha',
        'Pch':      'nadegas',
        'Tv':       'narcos',
        'Esporte':  'natacao',
    },
    'O': {
        'Cor':      'ouro',
        'Nome':     'odete',
        'Cep':      'otawa',
        'Famosos':  'olavo de carvalho',
        'Animal':   'ornintorrinto',
        'Marca':    'olx',
        'Mse':      'obesa',
        'Carro':    'opala',
        'Objeto':   'oculos',
        'Pch':      'olho',
        'Tv':       'os pinguins de madag',
        'Esporte':  'ondulacao',
    },
    'P': {
        'Cor':      'preto',
        'Nome':     'pedro',
        'Cep':      'portugal',
        'Famosos':  'paul mccartney',
        'Animal':   'peixe',
        'Marca':    'philips',
        'Mse':      'peidorrera',
        'Carro':    'pajero',
        'Objeto':   'piris',
        'Pch':      'palmas',
        'Tv':       'pecado mortal',
        'Esporte':  'pilates',
    },
    'R': {
        'Cor':      'roxo',
        'Nome':     'rodrigo',
        'Cep':      'roraima',
        'Famosos':  'rodrygo',
        'Animal':   'rato',
        'Marca':    'rener',
        'Mse':      'resmungona',
        'Carro':    'renegade',
        'Objeto':   'ralador',
        'Pch':      'radio',
        'Tv':       'rambo',
        'Esporte':  'rugby',
    },
    'S': {
        'Cor':      'salmao',
        'Nome':     'sergio',
        'Cep':      'sergipe',
        'Famosos':  'sergio ramos',
        'Animal':   'sabia',
        'Marca':    'subway',
        'Mse':      'sonsa',
        'Carro':    'sandero',
        'Objeto':   'saleiro',
        'Pch':      'seios',
        'Tv':       'sex education',
        'Esporte':  'surf',
    },
}

temas = ['Cor', 'Nome', 'Cep', 'Famosos', 'Animal', 'Marca', 'Mse', 'Carro', 'Objeto', 'Pch', 'Tv', 'Esporte']



class Stop:
    def __init__(self):
        self.driver_path = '/Users/bruno/Downloads/chromedriver 2'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_botao_class(self, css):
        btn = self.chrome.find_element_by_class_name(css)
        btn.click()

    def escrever_css_selector(self, valor, css_selector):
        local_escrever = self.chrome.find_element_by_css_selector(css_selector)

        local_escrever.send_keys(valor)

    def ler_letra(self, css_selsctor):
        letra = self.chrome.find_element_by_css_selector(css_selsctor).text
        return letra

    def responde(self, letra):
        print('O bot comecou a responder!!!')
        contador = 1

        while contador <= 12:
            contador += 1
            sleep(0.3)
            palavra = self.ler_letra(f'#screenGame > div:nth-child(2) > div.content > div > div:nth-child(1) > label:nth-child({contador}) > span')

            for tema in temas:
                processamento_2 = unicodedata.normalize("NFD", tema)
                processamento_2 = processamento_2.encode("ascii", "ignore")
                processamento_2 = processamento_2.decode("utf-8")

                if palavra == tema.upper():
                    self.escrever_css_selector(dicinario_palavras[letra][processamento_2.capitalize()], f'#screenGame > div:nth-child(2) > div.content > div > div:nth-child(1) > label:nth-child({contador}) > input[type="text"]')

stop = Stop()

try:
    print('Seja muito Bem vindo!!')
    stop.acessa('https://stopots.com/system/search')
    sleep(5)
    #stop.escrever_css_selector('19683', '#search')  ##########Precisa configurar
    sleep(1)
    #stop.clica_botao_class('room')
    sleep(2)
    #stop.clica_botao_class('icon-exclamation')
    sleep(1)
    #stop.escrever_css_selector('1234', '#popup > div > form > div.center > input[type="password"]')

    while True:
        liberar = int(input('Posso Liberar o Bot para a rodada? [1] - libera '))

        if liberar == 1:
            # inicio do jogo
            print('Bot liberado, comecaremos o jogo!')
            sleep(5)
            letra_do_jogo = stop.ler_letra('#letter > span')

            todas_letras = list(string.ascii_uppercase)

            # Inicio da rodada
            for letra in todas_letras:
                # sabemos a letra
                if letra_do_jogo == letra:
                    print(f'Maravilha! o Bot obteu a letra da rodada {letra}')
                    stop.responde(letra)
                    print('Conseguimos responder!!!')
        else:
            break


except Exception as e:
    print('Erro', e)
finally:
    print('Bot finalizado')
    stop.sair()
