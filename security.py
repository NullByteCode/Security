# O código a seguir foi desenvolvido em Python para a geração de senhas,
# lista de senhas, hashes e codificação em base64.
# GitHub: https://github.com/NullByteCode
# Code by: SAYKE - ISL

import base64
import hashlib
import random
import string
import sys

logo = """
███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝ 
╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  
███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║   
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝ 
"""
line = "---------------------------------------------------------------"


OPTION_PASSWD = "1"
OPTION_HASHS = "2"
OPTION_ENCODE = "3"
OPTION_WORDLIST = "4"
OPTION_QUIT = "0"
OPTION_ENTRY = ["1", "2", "3", "4", "0"]


def handle_keyboard_interrupt():
    print("\n", end='')
    print(line)
    print("ENCERRANDO O PROGRAMA.")
    print(line)
    sys.exit()


def passwd():
    try:
        print(line)
        tamanho = int(input("DIGITE A QUANTIDADE DE CARACTERES: "))
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(line)
        print("SUA SENHA: {}".format(senha))
        print(line)
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
    except ValueError:
        print(line)
        print("O TAMANHO DA SENHA DEVE SER UM NÚMERO INTEIRO POSITIVO.")
        print(line)
        sys.exit()


def hashes():
    try:
        print(line)
        mensagem = input("INSIRA O QUE DESEJA CRIPTOGRAFAR: ")
        print(line)
        if not mensagem:
            print("ERRO: A ENTRADA NÃO PODE SER VAZIA.")
            print(line)
            sys.exit()
        tipos_hash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
        tipo_hash = input(f"ESCOLHA O TIPO DE HASH ENTRE {tipos_hash} : ")
        print(line)
        if not tipos_hash:
            print("ERRO: A ENTRADA NÃO PODE SER VAZIA.")
            print(line)
            sys.exit()
        elif tipo_hash not in tipos_hash:
            print("ERRO: O TIPO DE HASH {} NÃO É SUPORTADO".format(tipo_hash,))
            print(line)
            sys.exit()
        elif tipo_hash in tipos_hash:
            hash_obj = hashlib.new(tipo_hash, mensagem.encode())
            hash_str = hash_obj.hexdigest()
            print("HASH {} = {}".format(tipo_hash.upper(), hash_str))
            print(line)
        else:
            print("OPÇÃO INVÁLIDA.")
            print(line)
            sys.exit()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


def encode():
    try:
        print(line)
        mensagem = input("INSIRA O QUE DESEJA CODIFICAR: ")
        print(line)
        if not mensagem:
            print("ERRO: A ENTRADA NÃO PODE SER VAZIA.")
            print(line)
            sys.exit()
        encoding = base64.b64encode(mensagem.encode()).decode()
        print("ALGORITIMO CODIFICADO: {}".format(encoding))
        print(line)
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


def wordlist():
    try:
        print(line)
        caracteres = string.ascii_letters + string.digits + string.punctuation
        numb = int(input("DIGITE O TAMANHO DAS SENHAS: "))
        print(line)
        num_senhas = int(input("DIGITE A QUANTIDADE DE SENHAS: "))
        print(line)
        arquivo = input("DIGITE O NOME DO ARQUIVO DE SAIDA: ")
        print(line)
        with open(arquivo, 'w') as arq:
            for senha in range(num_senhas):
                senha = ''.join(random.choice(caracteres) for _ in range(numb))
                arq.write(senha + '\n')
                print(senha)
                print(line)
            print("SENHAS GERADAS COM SUCESSO E SALVAS NO ARQUIVO: ", arquivo)
            print(line)
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
    except ValueError:
        print(line)
        print("O TAMANHO DAS SENHAS DEVE SER UM NÚMERO INTEIRO POSITIVO.")
        print(line)
        sys.exit()


def main():
    try:
        print(line)
        print(logo)
        print(line)
        print("1 - GERADOR DE SENHAS")
        print("2 - GERADOR DE HASHES")
        print("3 - GERAR CODIFICAÇÃO")
        print("4 - GERADOR DE LISTA DE SENHAS")
        print("0 - SAIR DO PROGRAMA")
        print(line)

        entry = input("SELECIONE A OPÇÃO: ")

        if entry == OPTION_PASSWD:
            passwd()
        elif entry == OPTION_HASHS:
            hashs()
        elif entry == OPTION_ENCODE:
            encode()
        elif entry == OPTION_WORDLIST:
            wordlist()
        elif entry == OPTION_QUIT:
            print(line)
            print("SAINDO!!!")
            print(line)
            sys.exit()
        elif entry != OPTION_ENTRY:
            print(line)
            print("MODO DE USO - ESCOLHA ENTRE AS OPÇOES: 1,2,3,4,0")
            print(line)
            sys.exit()
        elif not entry:
            print(line)
            print("ERRO: A ENTRADA NÃO PODE SER VAZIA.")
            print(line)
            sys.exit()
        else:
            print(line)
            print("OCORREU UM ERRO INESPERADO")
            print(line)
            sys.exit()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


if __name__ == "__main__":
    main()
