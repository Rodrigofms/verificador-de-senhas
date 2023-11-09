"""Importação das bibliotecas necessárias"""
import os
import hashlib
import requests


def clear():
    """Apaga o conteudo do console"""
    return os.system("cls")


def request_api_data(query):
    """Verifica se a api está funcionando"""
    url = "https://api.pwnedpasswords.com/range/" + query
    res = requests.get(url, timeout=10)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching {res.status_code}, veja se a API se encontra disponível"
        )
    return res


def get_leaks(hashes, hash_to_check):
    """Verifica se a senha foi comprometida"""
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def check_pwned(password):
    """Transforma a texto em hash1"""
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, rest = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_leaks(response, rest)


def main(args):
    """Diz quantas vezes a senha inserida foi comprometida ou não"""
    count = check_pwned(args)
    if count:
        print(f"A senha {args} foi comprometida {count}....")
    else:
        print(f"A senha {args} não foi comprometida!!!")


OPCAO1 = "s"
OPCAO2 = "n"

if __name__ == "__main__":
    print("Bem vindo ao verificador de senhas")
    print("Pressione enter para continuar")
    input()
    clear()
    while True:
        senha_Usuario = input(
            "Por favor, digite sua senha para verificar se foi comprometida: "
        )
        clear()

        while senha_Usuario == "":
            print("Por favor preencha o campo")
            senha_Usuario = input(
                "Por favor, digite sua senha para verificar se foi comprometida: "
            )
            clear()

        main(senha_Usuario)
        escolha = input("Deseja verificar mais uma senha S/N: ").lower()
        clear()

        while escolha != OPCAO1 and escolha != OPCAO2:
            print("Opção inválida")
            escolha = input("Deseja verificar mais uma senha S/N: ").lower()
            clear()

        if escolha == "s":
            clear()
            main(senha_Usuario)
        if escolha == "n":
            clear()
            print("Pressione enter para finalizar")
            input()
            clear()
            break
