class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self,data = None):
        if data:
            node = Node(data)
            self.root = node 
        else:
            self.root = None
    def simetric_traversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            print(end=' ')
            self.simetric_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.simetric_traversal(node.right)
            print(end=' ')

if __name__ == "__main__":

    tree = BinaryTree()
    n1 = Node("No livro")
    n2 = Node('está tudo')
    n3 = Node('as pessoas')
    n4 = Node('que dizem')
    n5 = Node('é o')
    n6 = Node('livros')
    n7 = Node('sentimos')
    n8 = Node('coisas')
    n9 = Node('boas')
    n10 = Node('ao lermos')

    n2.left = n1
    n2.right = n5
    n5.right = n3
    n3.left = n4
    n3.right = n6
    n6.left = n10
    n6.right = n8
    n8.left = n7
    n8.right = n9

    tree.root = n2
    tree.simetric_traversal()
    print()

            
