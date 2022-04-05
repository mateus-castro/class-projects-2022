from collections import defaultdict

class Grafo(object):
    def __init__(self, direcionado=False):
        self.adj = defaultdict(set)
        self.vertices_list = []
        self.direcionado = direcionado

    def adiciona_vertice(self, vertice):
        self.vertices_list.append(vertice)

    def get_vertices(self):
        #  Retorna a lista de vértices do grafo.
        return self.vertices_list

    def get_arestas(self):
        #  Retorna a lista de arestas do grafo.
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        #  Adiciona arestas ao grafo. 
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        #  Adiciona uma ligação (arco) entre os nodos 'u' e 'v'.
        #  Adiciona os vértices da aresta na lista caso não existam
        if not self.vertices_list.__contains__(u):
            self.vertices_list.append(u)
        if not self.vertices_list.__contains__(v):
            self.vertices_list.append(v)

        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        #  Existe uma aresta entre os vértices 'u' e 'v'? 
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]

# # # Cria a lista de arestas.
# arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]
# grafo = Grafo()
# grafo.adiciona_arestas(arestas)
# print(grafo.get_arestas())
# print(grafo.get_vertices())