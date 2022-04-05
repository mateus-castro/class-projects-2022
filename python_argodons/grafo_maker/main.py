from tracemalloc import stop
import grafo

class Main():
    
    def __init__(self):
        print("Bem vindo ao GrafoMaker!\n")
        self.impl_grafo = grafo.Grafo()
        self.menu()

    def menu(self):
        user_input = input("MENU:\n\t1. Adicionar vertice.\n\t2. Adicionar aresta.\n\t3. Mostrar informações do grafo.\n\t4. Sair (Você perderá as informações salvas de seu grafo).\n")
        
        if user_input == "1":
            self.adiciona_vertice()
        elif user_input == "2":
            self.adiciona_aresta()
        elif user_input == "3":
            self.mostra_info_grafo()
        elif user_input == "4":
            self.sair()
        else:
            print("Tarefa inválida. Confira as opções novamente.")
            self.menu()

    def adiciona_vertice(self):
        print("bla")
        vertice = input("Qual vértice deseja criar? ")
        self.impl_grafo.adiciona_vertice(vertice)
        self.menu()

    def adiciona_aresta(self):
        src = input("Insira o vértice de origem da aresta: ")
        dest = input("Agora insira o vértice de destino: ")
        peso = input("Por último informe o peso da aresta: ")
        self.impl_grafo.adiciona_arestas([(src, dest)])
        self.menu()

    def mostra_info_grafo(self):
        vertices = self.impl_grafo.get_vertices()
        arestas = self.impl_grafo.get_arestas()
        direc = self.impl_grafo.direcionado

        if len(vertices) > 0:
            print(f"Vértices: {vertices}")
        if len(arestas) > 0:
            print(f"Arestas: {arestas}")
        if len(vertices) == 0 and len(arestas) == 0:
            print("\nVocê ainda não inseriu nenhuma informação.\n")

        self.menu()

    def sair(self):
        print("Bye...")
        exit()
        

Main().menu()