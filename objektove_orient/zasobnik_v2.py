class Node:
    def __init__(self, value):
        self.value = value
        self.next = None




uzel_1 = Node(1)


uzel_2 = Node(2)
uzel_2.next = uzel_1


uzel_3 = Node(3)
uzel_3.next = uzel_2


print(uzel_3.value)
print(uzel_3.next.value)
print(uzel_3.next.next.value)