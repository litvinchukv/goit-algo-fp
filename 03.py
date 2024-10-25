import heapq

class Graph:
    def __init__(self):
        # Використовуємо словник для представлення графа. Ключ - вершина, значення - список суміжних вершин і ваг ребер
        self.vertices = {}

    def add_edge(self, u, v, weight):
        # Додаємо ребро з вершини u у вершину v з вагою weight
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))  # Для неорієнтованого графа додаємо двосторонній зв'язок

    def dijkstra(self, start):
        # Ініціалізуємо відстані до всіх вершин як нескінченність, а до стартової - 0
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        # Використовуємо пріоритетну чергу (бінарну купу)
        priority_queue = [(0, start)]  # Містить пари (відстань, вершина)
        heapq.heapify(priority_queue)

        # Словник для збереження шляху
        shortest_path_tree = {}

        while priority_queue:
            # Виймаємо вершину з мінімальною відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо знайдено коротший шлях до поточної вершини, пропускаємо її
            if current_distance > distances[current_vertex]:
                continue

            # Обробляємо всіх сусідів поточної вершини
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань і додаємо в чергу
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    shortest_path_tree[neighbor] = current_vertex

        return distances, shortest_path_tree

# Приклад використання:
def main():
    g = Graph()
    # Додаємо ребра у граф (u, v, вага)
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 3)

    # Викликаємо алгоритм Дейкстри від стартової вершини 'A'
    start_vertex = 'A'
    distances, shortest_path_tree = g.dijkstra(start_vertex)

    # Виведення найкоротших відстаней до всіх вершин
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex in distances:
        print(f"Вершина {vertex}: {distances[vertex]}")

if __name__ == "__main__":
    main()