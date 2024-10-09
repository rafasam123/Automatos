import graphviz
from collections import defaultdict, deque

class Automato:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

def ler_arquivo_automato(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    estados = linhas[0].strip().split()
    estado_inicial = linhas[1].strip()
    estados_finais = linhas[2].strip().split()
    
    transicoes = defaultdict(list)
    for linha in linhas[3:]:
        estado, simbolo, prox_estado = linha.strip().split()
        transicoes[(estado, simbolo)].append(prox_estado)
    
    return Automato(estados, estado_inicial, estados_finais, transicoes)

def estado_vazio(automato, estado):
    closure = {estado}
    stack = [estado]

    while stack:
        current = stack.pop()
        if (current, 'h') in automato.transicoes:  # Transição epsilon representada por 'h'
            for next_state in automato.transicoes[(current, 'h')]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    
    return closure


def converter_para_dfa(afnd):
    fecho_inicial = estado_vazio(afnd, afnd.estado_inicial)
    estados_dfa = {frozenset(fecho_inicial): 'A'}
    cont_estados = 1
    transicoes_dfa = {}
    estados_finais_dfa = set()
    
    estados_nao_marcados = deque([frozenset(fecho_inicial)])
    
    while estados_nao_marcados:
        conjunto_atual = estados_nao_marcados.popleft()
        estado_dfa_atual = estados_dfa[conjunto_atual]

        for simbolo in ['0', '1']:  # Alfabeto do AFD
            prox_estados = set()
            for estado in conjunto_atual:
                if (estado, simbolo) in afnd.transicoes:
                    for prox_estado in afnd.transicoes[(estado, simbolo)]:
                        prox_estados.update(estado_vazio(afnd, prox_estado))
            
            if prox_estados:
                prox_estados_frozenset = frozenset(prox_estados)
                if prox_estados_frozenset not in estados_dfa:
                    cont_estados += 1
                    estados_dfa[prox_estados_frozenset] = chr(ord('A') + cont_estados - 1)
                    estados_nao_marcados.append(prox_estados_frozenset)
                
                transicoes_dfa[(estado_dfa_atual, simbolo)] = estados_dfa[prox_estados_frozenset]
    
    for conjunto_estados, estado_dfa in estados_dfa.items():
        if any(estado in afnd.estados_finais for estado in conjunto_estados):
            estados_finais_dfa.add(estado_dfa)

    return Automato(
        estados=list(estados_dfa.values()),
        estado_inicial=estados_dfa[frozenset(fecho_inicial)],
        estados_finais=list(estados_finais_dfa),
        transicoes=transicoes_dfa
    )

def salvar_automato(caminho_arquivo, automato):
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(' '.join(automato.estados) + '\n')
        arquivo.write(automato.estado_inicial + '\n')
        arquivo.write(' '.join(automato.estados_finais) + '\n')
        
        for (estado, simbolo), prox_estados in automato.transicoes.items():
            for prox_estado in prox_estados:
                arquivo.write(f"{estado} {simbolo} {prox_estado}\n")

def visualizar_automato(automato, nome_arquivo):
    grafo = graphviz.Digraph()

    for (estado, simbolo), prox_estados in automato.transicoes.items():
        for prox_estado in prox_estados:
            grafo.edge(estado, prox_estado, label=simbolo)

    grafo.node(automato.estado_inicial, shape='circle', style='filled', fillcolor='lightgrey')

    for estado in automato.estados_finais:
        grafo.node(estado, shape='doublecircle')

    with open(f"{nome_arquivo}.dot", "w") as arquivo:
        arquivo.write(grafo.source)

    print(f"O arquivo {nome_arquivo}.dot foi gerado.")

def testar_palavras(dfa, caminho_palavras, caminho_saida):
    with open(caminho_palavras, 'r') as arquivo:
        palavras = arquivo.readlines()

    resultados = []
    for palavra in palavras:
        palavra = palavra.strip()
        estado_atual = dfa.estado_inicial
        
        for simbolo in palavra:
            if (estado_atual, simbolo) in dfa.transicoes:
                estado_atual = dfa.transicoes[(estado_atual, simbolo)]
            else:
                estado_atual = None
                break
        
        if estado_atual and estado_atual in dfa.estados_finais:
            resultados.append(f"{palavra} aceito")
        else:
            resultados.append(f"{palavra} nao aceito")
    
    with open(caminho_saida, 'w') as arquivo:
        for resultado in resultados:
            arquivo.write(resultado + '\n')

def main():
    caminho_afnd = "entrada.txt"
    caminho_afd = "saida.txt"
    caminho_palavras = "palavras.txt"
    caminho_resultado_palavras = "saida_palavras.txt"
    
    afnd = ler_arquivo_automato(caminho_afnd)
    afd = converter_para_dfa(afnd)
    salvar_automato(caminho_afd, afd)
    visualizar_automato(afnd, "grafo_afnd")
    visualizar_automato(afd, "grafo_afd")
    
    testar_palavras(afd, caminho_palavras, caminho_resultado_palavras)

if __name__ == "__main__":
    main()
