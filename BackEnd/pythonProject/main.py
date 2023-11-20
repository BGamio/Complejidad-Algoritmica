import csv
#import graphviz
import heapq as hq
import math

def read_csv(file_path):
    """
    Lee el archivo CSV y retorna los datos como una lista de diccionarios.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {file_path}")
        return []

def build_graph(data):
    """
    Construye el grafo utilizando listas de adyacencia.
    """
    street_graph = {}

    for i in range(len(data) - 1):
        current_node = (
            (int(data[i]['ADDRESS_NUMBER']) if data[i]['ADDRESS_NUMBER'].isdigit() else 0, data[i]['STREET_NAME'])
        )
        next_node = (
            (int(data[i + 1]['ADDRESS_NUMBER']) if data[i + 1]['ADDRESS_NUMBER'].isdigit() else 0,
             data[i + 1]['STREET_NAME'])
        )

        if current_node not in street_graph:
            street_graph[current_node] = {}

        weight = ((float(data[i + 1]['X_COORDINATE']) - float(data[i]['X_COORDINATE'])) ** 2 +
                  (float(data[i + 1]['Y_COORDINATE']) - float(data[i]['Y_COORDINATE'])) ** 2) ** 0.5
        street_graph[current_node][next_node] = weight

    return street_graph

def dijkstra(graph, start, end):
    """
    Aplica el algoritmo de Dijkstra para encontrar el camino más corto entre dos nodos en el grafo.
    """
    nodes = list(graph)
    node_index_map = {node: i for i, node in enumerate(nodes)}
    visited = set()
    cost = [math.inf] * len(graph)
    path = [-1] * len(graph)

    start_index = node_index_map[start]
    end_index = node_index_map[end]

    cost[start_index] = 0
    pqueue = [(0, start_index)]

    while pqueue:
        g, u = hq.heappop(pqueue)
        if u in visited:
            continue

        visited.add(u)

        for v, w in graph.get(nodes[u], {}).items():
            v_index = node_index_map.get(v, None)
            if v_index is not None and v_index not in visited:
                f = g + w
                if f < cost[v_index]:
                    cost[v_index] = f
                    path[v_index] = u
                    hq.heappush(pqueue, (f, v_index))

    # Reconstruye el camino desde el final hasta el principio
    current_node = end_index
    shortest_path = []
    while current_node != -1:
        shortest_path.insert(0, nodes[current_node])
        current_node = path[current_node]

    return shortest_path

def visualize_graph(graph, path):
    """
    Visualiza el grafo con el camino más corto resaltado.
    """
    dot = graphviz.Digraph(format='png')

    for node, neighbors in graph.items():
        node_str = f"{node[0]}_{node[1]}"
        if node in path:
            dot.node(node_str, style='filled', fillcolor='yellow')
        else:
            dot.node(node_str)

        for neighbor, weight in neighbors.items():
            neighbor_str = f"{neighbor[0]}_{neighbor[1]}"
            if node in path and neighbor in path:
                dot.edge(node_str, neighbor_str, label=str(weight), color='red')
            else:
                dot.edge(node_str, neighbor_str, label=str(weight))

    dot.render('graph_with_path', format='png', cleanup=True)

if __name__ == "__main__":
    # Lee el archivo CSV
    file_path = 'Puntos de direcciones_4.csv'
    data = read_csv(file_path)

    if not data:
        # Manejo del caso en que no se puede leer el archivo
        print("No se pueden cargar los datos del archivo. Saliendo.")
    else:
        # Construye el grafo
        street_graph = build_graph(data)

        # Solicita al usuario que ingrese el nodo de inicio
        start_number = input("Ingrese el número de la calle de inicio: ")
        start_street = input("Ingrese el nombre de la calle de inicio: ")
        start_node = (int(start_number), start_street)

        # Solicita al usuario que ingrese el nodo de fin
        end_number = input("Ingrese el número de la calle de fin: ")
        end_street = input("Ingrese el nombre de la calle de fin: ")
        end_node = (int(end_number), end_street)

        # Verifica que los nodos ingresados por el usuario existan en el grafo
        if start_node not in street_graph or end_node not in street_graph:
            print("Error: Uno o ambos nodos ingresados no existen en el grafo.")
        else:
            # Aplica el algoritmo de Dijkstra
            shortest_path = dijkstra(street_graph, start_node, end_node)

            # Visualiza el grafo con el camino más corto resaltado
            #visualize_graph(street_graph, shortest_path)

            # Imprime el resultado
            print("Ruta más corta:", shortest_path)
