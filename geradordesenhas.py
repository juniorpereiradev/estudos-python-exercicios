import secrets
import string
from datetime import datetime

TAMANHO = 10
ARQUIVO_NOTA = "senhas_geradas.txt"


def gerar_senha(tamanho=TAMANHO):
    conjuntos = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()_-+=<>?/{}[]~",
    ]


    senha = [secrets.choice(c) for c in conjuntos]

    alfabeto = "".join(conjuntos)
    senha += [secrets.choice(alfabeto) for _ in range(tamanho - len(senha))]

    secrets.SystemRandom().shuffle(senha)
    return "".join(senha[:tamanho])


CABECALHO = f"{'ID':<5} | {'Data/Hora':<19} | {'Senha'}\n" + "-" * 45 + "\n"


def proximo_id():
    try:
        with open(ARQUIVO_NOTA, "r", encoding="utf-8") as f:
            linhas = f.readlines()[2:]  
            linhas = [l for l in linhas if l.strip()]
            if not linhas:
                return 1
            ultimo_id = linhas[-1].split("|")[0].strip()
            return int(ultimo_id) + 1
    except FileNotFoundError:
        return 1


def salvar_nota(senha, id_senha):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    arquivo_existe = False
    try:
        with open(ARQUIVO_NOTA, "r", encoding="utf-8"):
            arquivo_existe = True
    except FileNotFoundError:
        pass

    with open(ARQUIVO_NOTA, "a", encoding="utf-8") as f:
        if not arquivo_existe:
            f.write(CABECALHO)
        f.write(f"{id_senha:<5} | {agora:<19} | {senha}\n")


def main():
    id_senha = proximo_id()
    senha = gerar_senha()
    salvar_nota(senha, id_senha)
    print(f"ID {id_senha} - Senha gerada: {senha}")
    print(f"Tabela atualizada em: {ARQUIVO_NOTA}")


if __name__ == "__main__":
    main()