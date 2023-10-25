class MaquinaDeTuring:
    def __init__(self, fita, estado_inicial, regras_de_transicao):
        # Inicializa a Máquina de Turing com uma fita, estado inicial e regras de transição
        self.fita = fita
        self.posicao_cabeca = 0  # Inicializa a posição da cabeça de leitura/gravação na fita
        self.estado_atual = estado_inicial  # Define o estado inicial
        self.regras_de_transicao = regras_de_transicao  # Define as regras de transição

    def executar(self):
        # Enquanto o estado atual não for "parar", continue a execução
        while self.estado_atual != "parar":
            # Lê o símbolo na posição atual da cabeça de leitura
            simbolo_atual = self.fita[self.posicao_cabeca]

            # Verifica se existe uma regra de transição para o estado atual e o símbolo atual
            if (self.estado_atual, simbolo_atual) not in self.regras_de_transicao:
                break  # Se não houver regra, pare a execução

            # Obtém a próxima ação da regra de transição
            proximo_estado, escrever_simbolo, direcao_movimento = self.regras_de_transicao[(self.estado_atual, simbolo_atual)]

            # Escreve o novo símbolo na posição atual da cabeça de gravação
            self.fita[self.posicao_cabeca] = escrever_simbolo

            # Move a cabeça de leitura/gravação com base na direção especificada
            if direcao_movimento == "L":
                self.posicao_cabeca -= 1  # Move para a esquerda
            elif direcao_movimento == "R":
                self.posicao_cabeca += 1  # Move para a direita

            # Atualiza o estado atual
            self.estado_atual = proximo_estado

    def obter_conteudo_da_fita(self):
        # Retorna o conteúdo da fita após a execução
        return self.fita
