"""
Компания OOO "Предки − наше все" занимается построением генеалогического древа.
Так оказалось, что вместо стажировки в Яндексе вы
решили пойти работать в эту компанию для того, чтобы оплатить свое образование. К несчастью, данные о предках
ваших клиентов постоянно меняются, поэтому часто приходится его редактировать. Удивительным образом вы заметили,
что генеалогического древа для текущего клиента является бинарным деревом, где в вершине значение является возрастом
данного человека. Дабы автоматизировать процесс и ускорить процесс подготовки проекта, вы решили запрогать все
редактирование и трассировку с помощью следующих комманд:

insert x − добавить нового человека с возрастом x в древо.
Если в дереве уже есть человек с возрастом x, то добавлять нового не надо.

delete x − удалить из дерева чевловека с возрастом x
Если человека с возрастом x в древе нет, ничего делать не надо.

exists x− если есть человек с возрастом x есть в древе, вывести "true", если нет - "false".

next x − вывести минимальный возраст в древе, строго больший x, или "none", если такого нет.

prev x − вывести максимальный возраст в древе, строго меньший x, или "none", если такого нет.
В древо помещаются и извлекаются только целые числа, не превышающие по модулю 109

Входные данные
Операций с древом, их количество не превышает 100.

Выходные данные
Выведите последовательно результат выполнения всех операций exists, next, prev. Каждый ответ на новой строчке.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self._insert_recursive(self.root, x)

    def _insert_recursive(self, node, x):
        if x < node.value:
            if node.left is None:
                node.left = Node(x)
            else:
                self._insert_recursive(node.left, x)
        elif x > node.value:
            if node.right is None:
                node.right = Node(x)
            else:
                self._insert_recursive(node.right, x)

    def delete(self, x):
        self.root = self._delete_recursive(self.root, x)

    def _delete_recursive(self, node, x):
        if node is None:
            return node
        if x < node.value:
            node.left = self._delete_recursive(node.left, x)
        elif x > node.value:
            node.right = self._delete_recursive(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.age)
        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def exists(self, x):
        return self._exists_recursive(self.root, x)

    def _exists_recursive(self, node, x):
        if node is None:
            return "false"
        if x == node.value:
            return "true"
        elif x < node.value:
            return self._exists_recursive(node.left, x)
        else:
            return self._exists_recursive(node.right, x)

    def next(self, x):
        return self._next_recursive(self.root, x)

    def _next_recursive(self, node, x):
        if node is None:
            return "none"
        if x < node.value:
            result = self._next_recursive(node.left, x)
            if result == "none":
                return node.value
            return result
        else:
            return self._next_recursive(node.right, x)

    def prev(self, x):
        return self._prev_recursive(self.root, x)

    def _prev_recursive(self, node, x):
        if node is None:
            return "none"
        if x > node.value:
            result = self._prev_recursive(node.right, x)
            if result == "none":
                return node.value
            return result
        else:
            return self._prev_recursive(node.left, x)


def main():
    tree = BinaryTree()
    while True:
        try:
            line = input()
            data = line.split()
            if data[0] == 'insert':
                tree.insert(int(data[1]))
            elif data[0] == 'exists':
                result = tree.exists(int(data[1]))
                print(result)
            elif data[0] == 'next':
                result = tree.next(int(data[1]))
                print(result)
            elif data[0] == 'prev':
                result = tree.prev(int(data[1]))
                print(result)
            elif data[0] == 'delete':
                tree.delete(int(data[1]))
            else:
                break
        except (ValueError, EOFError):
            return


if __name__ == "__main__":
    main()
