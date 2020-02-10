def cria_dici(texto):
    palavras = texto.split()
    dici = {}
    for palavra in palavras:
        if palavra not in dici:
            dici[palavra] = 1
        else:
            dici[palavra] += 1
    return dici


if __name__ == "__main__":
    cria_dici()