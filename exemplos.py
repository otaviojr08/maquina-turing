from MaquinaTuring import MaquinaDeTuring


# Verifica se termina com 'aa'
def exemplo1():
    # Defina as regras de transição para verificar se a entrada termina com "aa"
    regras_de_transicao = {
        ("q0", "a"): ("q1", "a", "R"),  # Move para a direita mantendo 'a' na fita
        ("q0", "B"): ("q0", "B", "R"),  # Move para a direita sem alterar a fita
        ("q1", "a"): ("q2", "a", "R"),  # Move para a direita mantendo 'a' na fita
        ("q1", "B"): ("q1", "B", "R"),  # Move para a direita sem alterar a fita
        ("q2", "a"): ("q2", "a", "R"),  # Move para a direita mantendo 'a' na fita
        ("q2", "B"): (
            "aceita",
            "B",
            "N",
        ),  # Aceita a entrada quando encontra "B" após "aa"
        ("q2", "X"): ("q0", "X", "R"),  # Volta ao estado inicial após encontrar "aa"
    }

    entrada = ["a", "a", "a", "a", "B"]
    estado_inicial = "q0"
    mt = MaquinaDeTuring(entrada, estado_inicial, regras_de_transicao)
    mt.executar()

    # Verifique se a entrada foi aceita
    if mt.estado_atual == "aceita":
        print("A entrada termina com 'aa'")
    else:
        print("A entrada não termina com 'aa'")


# Palavra de entrada contém apenas um 'b'
def exemplo2():
    # Defina as regras de transição para verificar se a palavra de entrada possui somente 1 "b"
    regras_de_transicao = {
        ("q0", "a"): ("q0", "a", "R"),  # Move para a direita mantendo 'a' na fita
        ("q0", "b"): ("q1", "b", "R"),  # Move para a direita mantendo 'b' na fita
        ("q0", "B"): (
            "parar",
            "B",
            "N",
        ),  # Encontra um espaço em branco (fim da entrada)
        ("q1", "a"): ("q1", "a", "R"),  # Move para a direita mantendo 'a' na fita
        ("q1", "b"): ("rejeita", "b", "N"),  # Rejeita a entrada se encontrar outro "b"
        ("q1", "B"): (
            "aceita",
            "B",
            "N",
        ),  # Aceita a entrada quando encontra espaço em branco após um "b"
    }

    entrada = ["a", "a", "b", "B"]

    estado_inicial = "q0"
    mt = MaquinaDeTuring(entrada, estado_inicial, regras_de_transicao)
    mt.executar()
    resultado = mt.obter_conteudo_da_fita()

    # Verifique se a entrada foi aceita
    if mt.estado_atual == "aceita":
        print("A entrada possui somente um 'b'")
    else:
        print("A entrada não possui somente um 'b'")


# Troca 'a' por 'b'
def exemplo3():
    # Defina as regras de transição para trocar 'a' por 'b'
    regras_de_transicao = {
        ("q0", "a"): ("q0", "b", "R"),  # Troca 'a' por 'b' e move para a direita
        ("q0", "b"): ("q0", "b", "R"),  # Move para a direita mantendo 'b' na fita
        ("q0", "B"): (
            "aceita",
            "B",
            "N",
        ),  # Aceita a entrada quando encontra espaço em branco (fim da entrada)
    }

    entrada = ["a", "a", "a", "a", "B"]

    estado_inicial = "q0"
    mt = MaquinaDeTuring(entrada, estado_inicial, regras_de_transicao)
    mt.executar()
    resultado = mt.obter_conteudo_da_fita()

    # Imprime a entrada após a substituição
    print("Entrada após a substituição: " + "".join(resultado))
