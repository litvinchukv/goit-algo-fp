import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Клас вузла дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000080"  # Початковий колір темно-синій
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор

# Додає вузли та ребра до графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Відображає дерево з оновленими кольорами
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для інтерполяції кольорів (від темного до світлого синього)
def get_color_by_order(order, total_steps):
    # Темний синій -> Світлий синій
    start_color = [0, 0, 128]  # #000080
    end_color = [18, 150, 240]  # #1296F0
    ratio = order / total_steps
    new_color = [
        int(start_color[i] + (end_color[i] - start_color[i]) * ratio)
        for i in range(3)
    ]
    return "#{:02x}{:02x}{:02x}".format(new_color[0], new_color[1], new_color[2])

# Обхід в глибину (DFS) з використанням стека та візуалізацією
def dfs_with_stack(node, total_steps):
    stack = [node]  # Використовуємо стек для обходу
    order = 0

    while stack:
        current_node = stack.pop()

        if current_node:
            # Присвоюємо новий колір вузлу
            current_node.color = get_color_by_order(order, total_steps)
            draw_tree(root)  # Оновлюємо візуалізацію
            order += 1

            # Додаємо правого нащадка до стека, потім лівого (щоб лівий оброблявся першим)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

# Обхід в ширину (BFS) з використанням черги та візуалізацією
def bfs_with_queue(node, total_steps):
    queue = deque([node])
    order = 0

    while queue:
        current_node = queue.popleft()

        if current_node:
            # Присвоюємо новий колір вузлу
            current_node.color = get_color_by_order(order, total_steps)
            draw_tree(root)  # Оновлюємо візуалізацію
            order += 1

            # Додаємо нащадків до черги
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

# Створюємо дерево для демонстрації
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Вибір типу обходу
traversal_type = input("Виберіть тип обходу (dfs/bfs): ").strip().lower()

# Підраховуємо загальну кількість вузлів
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

total_steps = count_nodes(root)

# Виконання обходу з візуалізацією
if traversal_type == "dfs":
    dfs_with_stack(root, total_steps)
elif traversal_type == "bfs":
    bfs_with_queue(root, total_steps)
else:
    print("Невідомий тип обходу")