from v0_0_vigenere_funcoes import *
from pathlib import Path

#MAIN
def main():
    mensagem = Path('desafio2.txt').read_text()

    chave = "chave".upper()
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".upper()


    #Gera indices que serão usados como base, na hora de trocar os char. Com essa abordagem de índice, consigo cifrar qualquer char, desde que esteja previsto na variavel alfabeto.
    letra_para_indice = dict(zip(alfabeto, range(len(alfabeto))))
    indice_para_letra = dict(zip(range(len(alfabeto)), alfabeto))

    #trata a mensagem, retirando acentos
    mensagem_tratada = tratar_mensagem(mensagem)
    mensagem_tratada = ''.join(x.upper() for x in mensagem_tratada if x.isalpha())	
    print("\nmensagem tratada:", mensagem_tratada,"\n") 

    #gera a chave ciclica que será usada, igualando ao tamanho da mensagem
    chave_ciclica = gerar_chave_ciclica(mensagem_tratada,chave)
    print("chave cilcica   :", chave_ciclica,"\n")

    #de-cifra a mensagem
    mensagem_descifrada = decifrar(mensagem_tratada, chave_ciclica, letra_para_indice, indice_para_letra, alfabeto)
    print("Mensagem De-Cifrada:", mensagem_descifrada,"\n")

main()