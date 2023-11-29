"""
Несмотря на все ваши старания, новогодняя бинарная ёлка в ИТМО все равно упала. Недолго думая, руководство решило
обратиться за помощью к уважаемым коллегам из нового физтеха. Проведя расчеты и эксперименты, физики предложили
вам такое решение - сделать из обычного бинарного дерева бинарное дерево поиска и нарядить дерево так, чтобы никакие
две ветки не отличались высотой более чем на 1.

Входные данные
В первой строчке дано n (1 ≤ n ≤ 106) - количество вершин.
Во второй строчке дано n чисел (−109 ≤ ai ≤ 109), разделенных пробелом, - количество украшений в вершине дерева,
отсортированных по возрастанию. Также не существует двух таких вершин, количества украшений которых одинаковы.

Выходные данные
Вывести бинарное дерево через preorder обход. В случае нескольких возможных ответов нужно вывести тот,
в котором корень каждого поддерева минимально возможный
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sortedArrayToBST(arr):
    if not arr:
        return None

    low = 0
    hight = len(arr) - 1
    mid = (low + hight) // 2
    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])

    return root


def preorderTraversal(root):
    if root:
        print(root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)


n = int(input())
arr = list(map(int, input().split()))
print(arr)

root = sortedArrayToBST(arr)

preorderTraversal(root)
