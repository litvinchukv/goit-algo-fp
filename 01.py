class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Метод для додавання елемента в список
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    # Метод для виведення списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

# Функція для поділу списку на дві половини
def split_list(head):
    slow = head
    fast = head

    if not head or not head.next:
        return head, None

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None
    return head, middle

# Функція для злиття двох відсортованих списків
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

# Основна функція для сортування злиттям
def merge_sort(head):
    if not head or not head.next:
        return head

    left, right = split_list(head)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted_lists(left, right)

def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next
if __name__ == "__main__":
    # Створення списку
    llist = LinkedList()
    llist.append(3)
    llist.append(1)
    llist.append(2)
    llist.append(5)

    print("Оригінальний список:")
    llist.print_list()

    # Реверсування списку
    reverse_list(llist)
    print("Після реверсування:")
    llist.print_list()

    # Сортування злиттям
    llist.head = merge_sort(llist.head)
    print("Після сортування:")
    llist.print_list()

    # Об'єднання двох відсортованих списків
    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(3)
    llist1.append(5)

    llist2 = LinkedList()
    llist2.append(2)
    llist2.append(4)
    llist2.append(6)

    merged_list = LinkedList()
    merged_list.head = merge_two_sorted_lists(llist1.head, llist2.head)
    print("Об'єднаний список:")
    merged_list.print_list()