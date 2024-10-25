import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла для візуалізації
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для побудови бінарної купи з масиву
def build_heap(arr):
    nodes = [Node(val) for val in arr]  # Створюємо вузли для кожного елемента масиву

    # Встановлюємо лівих і правих нащадків для вузлів
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]  # Повертаємо кореневий вузол

# Відображення бінарної купи
def visualize_heap(arr):
    heap_root = build_heap(arr)  # Побудова бінарної купи з масиву
    draw_tree(heap_root)  # Відображення дерева купи
    
if __name__ == "__main__":
    # Приклад використання
    arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]  # Масив для бінарної купи
    visualize_heap(arr)