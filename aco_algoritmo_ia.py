import random
import numpy as np
import pandas as pd

def atribuir_valores_aleatorios_normais(dados, media=5, desvio_padrao=2):
    for cidade in dados['Municipio'].unique():
        dados.loc[dados['Municipio'] == cidade, 'Valor de Compra'] = np.random.normal(media, desvio_padrao, len(dados[dados['Municipio'] == cidade]))
    dados['Valor de Compra'] = dados['Valor de Compra'].clip(lower=3)
    return dados

class FormigasColonia:
    def __init__(self, cidades, dados, n_formigas, n_iteracoes, evaporacao, alpha=1, beta=2):
        self.cidades = cidades
        self.dados = dados
        self.n_formigas = n_formigas
        self.n_iteracoes = n_iteracoes
        self.evaporation = evaporacao
        self.alpha = alpha 
        self.beta = beta  

        self.feromonio = np.ones((len(cidades), len(cidades)))
        self.heuristica = self.calcula_heuristica()
        #print(self.heuristica)

    def calcula_heuristica(self):
        heuristica = np.zeros((len(self.cidades), len(self.cidades)))
        #print(heuristica)
        produto = 'GASOLINA'

        for i, cidade1 in enumerate(self.cidades):
            for j, cidade2 in enumerate(self.cidades):
                if i != j:
                    # Filtra os dados de venda e compra para cada cidade
                    venda_c1 = self.dados[(self.dados['Municipio'] == cidade1) & 
                                          (self.dados['Produto'] == produto)]['Valor de Venda'].mean()
                    compra_c2 = self.dados[(self.dados['Municipio'] == cidade2) & 
                                           (self.dados['Produto'] == produto)]['Valor de Compra'].mean()
                    
                    print(f"Venda de {cidade1}: {venda_c1:.2f}, Compra de {cidade2}: {compra_c2:.2f}") 
                    
                    # Calcula a heurística como a diferença de venda e compra
                    heuristica[i][j] = max(venda_c1 - compra_c2, 0)
                    print(f"Heurística de {cidade1} para {cidade2}: {heuristica[i][j]:.2f}")  
                   
        return heuristica
    
    def calcula_probabilidade(self, cidade_atual, cidade_destino):
        # Verifique se o par de cidades tem um valor de feromônio e heurística válidos
        i, j = self.cidades.index(cidade_atual), self.cidades.index(cidade_destino)
        feromonio = self.feromonio[i, j]
        heuristica = self.heuristica[i, j]

        
        alfa = 1
        beta = 2

        # Cálculo da probabilidade usando a fórmula típica
        return (feromonio ** alfa) * (heuristica ** beta)

    def escolher_proxima_cidade(self, cidade_atual, cidades_disponiveis):
        probabilidades = [self.calcula_probabilidade(cidade_atual, cidade) for cidade in cidades_disponiveis]    
        probabilidades = [0 if not np.isfinite(p) else p for p in probabilidades]
    
        if sum(probabilidades) == 0:
            probabilidades = [1 for _ in cidades_disponiveis]  
    
        return random.choices(cidades_disponiveis, weights=probabilidades)[0]

    def atualizar_feromonio(self, rotas):
        self.feromonio *= (1 - self.evaporation)
        for rota, lucro in rotas:
            for i in range(len(rota) - 1):
                cidade1, cidade2 = rota[i], rota[i + 1]
                i, j = self.cidades.index(cidade1), self.cidades.index(cidade2)
                self.feromonio[i][j] += lucro

    def otimizar(self, cidade_inicial):
        melhor_rota = None
        melhor_lucro = -np.inf  # Inicia com um valor muito baixo
        for _ in range(self.n_iteracoes):
            rotas = []
            for _ in range(self.n_formigas):
                rota = [cidade_inicial]
                cidades_disponiveis = set(self.cidades) - {cidade_inicial}
                lucro_total = 0

                while cidades_disponiveis:
                    cidade_atual = rota[-1]
                    proxima_cidade = self.escolher_proxima_cidade(cidade_atual, list(cidades_disponiveis))
                    lucro_total += self.heuristica[self.cidades.index(cidade_atual)][self.cidades.index(proxima_cidade)]
                    rota.append(proxima_cidade)
                    cidades_disponiveis.remove(proxima_cidade)

                rotas.append((rota, lucro_total))

            self.atualizar_feromonio(rotas)

            # Seleciona a melhor rota com o maior lucro
            melhor_rota_atual = max(rotas, key=lambda x: x[1])
            if melhor_rota_atual[1] > melhor_lucro:
                melhor_rota = melhor_rota_atual[0]
                melhor_lucro = melhor_rota_atual[1]

        return melhor_rota, melhor_lucro

def carregar_dados(arquivo_csv):
    dados = pd.read_csv(arquivo_csv, decimal=',',delimiter=';', on_bad_lines='skip')
    print(dados.head())
    return dados

# Exemplo de uso
cidades = ['VITORIA DA CONQUISTA', 'BRASILIA', 'NOVA IGUACU', 'TERESINA', 'SAO PAULO', 'CURITIBA', 
           'BELO HORIZONTE', 'VINHEDO', 'PALMAS', 'GUARUJA']  
dados = carregar_dados('data/Precos_semestrais_AUTOMOTIVOS_2024.01.csv')

# Atribuir valores aleatórios de compra
dados = atribuir_valores_aleatorios_normais(dados)

ant_colony = FormigasColonia(cidades, dados, n_formigas=10, n_iteracoes=100, evaporacao=0.1)
melhor_rota, lucro = ant_colony.otimizar('BRASILIA')

print(f"Melhor rota: {melhor_rota}")
print(f"Lucro esperado: {lucro:.2f}")
