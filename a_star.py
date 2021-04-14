import math
import dists

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """

    # Apenas para facilitar a chamada
    a = dists.dists
    b = dists.straight_line_dists_from_bucharest

    # Inicializa a lista de expansões com a origem (start)
    expansions = [
        Node(start, 0, b.get(start))
    ]
    loop = 0
    while (True):

        # Busca qual é o nó com melhor trajeto até o momento
        best_node = None
        for i in expansions:
            if (best_node == None or i.total() < best_node.total()):
                best_node = i

        # Caso o o melhor nó seja o destino (goal) para o loop
        if (best_node != None and best_node.name == goal):
            print(f'**** Goal ****: {best_node}')
            break

        # Remove e imprime o melhor nó, pois ele sempre será o melhor caso não remova
        expansions.remove(best_node)
        print(f"Best node: {best_node}")
        
        # Faz a expansão do melhor nó
        for i in a.get(best_node.name):
            node = Node( 
                i[0], # nome da cidade
                i[1] + best_node.distance, # distancia é a distância entre as cidades + distancia total percorrida
                b.get(i[0]) # distancia da cidade até o destino (goal)
            )
            # Insere e imprime nó na expansão
            expansions.append( node )
            print(f'Expand: {node}')

        # Apenas para saber quantas expansões foram necessárias
        loop += 1
        print ("loop: " + str(loop))

# Classe para armazenar o nó
class Node:
    def __init__(self, name, distance, goal_distance):
        self.name = name
        self.distance = distance
        self.goal_distance = goal_distance

    def total(self):
        return self.distance + self.goal_distance
    
    def __str__(self):
        return f"Name: {self.name} Total: {self.distance + self.goal_distance} Distance: {self.distance} Goal Distance: {self.goal_distance}"

# Main
def main():
    # Para testar basta alterar o nome da cidade
    a_star('Arad')

if __name__ == "__main__":
    main()