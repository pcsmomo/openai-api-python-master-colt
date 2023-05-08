class Node:
    """
    Represents a node in a Binary Search Tree.
    """

    def __init__(self, data: int, leftChild=None, rightChild=None) -> None:
        """
        Initialize the node with a data, left and right child.

        :param data: The value of the node.
        :param leftChild: The left child of the node.
        :param rightChild: The right child of the node.
        """
        self.data = data
        self.leftChild = leftChild or None
        self.rightChild = rightChild or None

    def insert(self, data: int) -> None:
        """
        Insert a node with a given data value into the Binary Search Tree.

        :param data: The value of the node to be inserted.
        """
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)

    def search(self, val: int) -> str:
        """
        Search for a node with a given data value in the Binary Search Tree.

        :param val: The value of the node to be searched.
        :return: A string representation of whether the node is found or not.
        """
        if self.data == val:
            return str(val) + " is found in the BST"
        elif val < self.data:
            return self.leftChild.search(val) if self.leftChild else str(val) + " is not found in the BST"
        else:
            return self.rightChild.search(val) if self.rightChild else str(val) + " is not found in the BST"

    def get_nodes(self) -> list[int]:
        """
        Get a list of nodes in the Binary Search Tree.

        :return: A list of integers representing the nodes in the Binary Search Tree.
        """
        nodes = []
        if self.leftChild:
            nodes.extend(self.leftChild.get_nodes())
        nodes.append(self.data)
        if self.rightChild:
            nodes.extend(self.rightChild.get_nodes())
        return nodes


def build_tree() -> Node:
    """
    Build a Binary Search Tree and insert some values into it.
    """
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)
    return root


def test_search(root: Node) -> None:
    """
    Test the search method of the Binary Search Tree.

    :param root: The root node of the Binary Search Tree.
    """
    print(root.search(7))
    print(root.search(14))


if __name__ == "__main__":
    tree = build_tree()
    print(tree.get_nodes())
    test_search(tree)
