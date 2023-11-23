import csv
import heapq as hq
import math
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

street_graph = None

def read_csv(file_path):

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {file_path}")
        return []


def build_graph(data):

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


    current_node = end_index
    shortest_path = []
    while current_node != -1:
        shortest_path.insert(0, nodes[current_node])
        current_node = path[current_node]

    return shortest_path

# def prim(graph, start, end):
#     nodes = list(graph)
#     node_index_map = {node: i for i, node in enumerate(nodes)}
#     visited = set()
#     cost = [math.inf] * len(graph)
#     parent = [-1] * len(graph)
#
#     start_index = node_index_map[start]
#     end_index = node_index_map[end]
#
#     cost[start_index] = 0
#     pqueue = [(0, start_index)]
#
#     while pqueue:
#         u_cost, u = hq.heappop(pqueue)
#         if u in visited:
#             continue
#
#         visited.add(u)
#
#         for v, w in graph.get(nodes[u], {}).items():
#             v_index = node_index_map.get(v, None)
#             if v_index is not None and v_index not in visited and w < cost[v_index]:
#                 cost[v_index] = w
#                 parent[v_index] = u
#                 hq.heappush(pqueue, (w, v_index))
#
#     # Reconstruye el camino desde el final hasta el principio
#     current_node = end_index
#     shortest_path = []
#     while current_node != -1:
#         shortest_path.insert(0, nodes[current_node])
#         current_node = parent[current_node]
#
#     return shortest_path

@app.route('/get_shortest_path', methods=['POST'])
def get_shortest_path():
    try:
        global street_graph


        request_data = request.get_json()


        start_node = (
            int(request_data['start']['ADDRESS_NUMBER']),
            request_data['start']['STREET_NAME']
        )
        end_node = (
            int(request_data['end']['ADDRESS_NUMBER']),
            request_data['end']['STREET_NAME']
        )


        if start_node not in street_graph or end_node not in street_graph:
            return jsonify({"error": "Uno o ambos nodos ingresados no existen en el grafo."}), 400


        shortest_path = dijkstra(street_graph, start_node, end_node)


        return jsonify({"shortest_path": shortest_path})

    except Exception as e:

        print("Error al procesar la solicitud:", str(e))
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":

    file_path = 'Puntos de direcciones_4.csv'
    data = read_csv(file_path)

    if not data:

        print("No se pueden cargar los datos del archivo. Saliendo.")
    else:

        street_graph = build_graph(data)

    app.run(debug=True, port=5000)
