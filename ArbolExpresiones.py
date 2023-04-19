import graphviz

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def build_expression_tree(expression):
    tokens = expression.split()
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            node = Node(token)
            node.right_child = stack.pop()
            node.left_child = stack.pop()
            stack.append(node)
        else:
            stack.append(Node(token))
    return stack.pop()

def visualize_expression_tree(root):
    dot = graphviz.Digraph()
    _visualize_expression_tree(root, dot)
    dot.render('expression_tree', view=True)

def _visualize_expression_tree(node, dot):
    dot.node(str(id(node)), node.value)
    if node.left_child is not None:
        dot.edge(str(id(node)), str(id(node.left_child)))
        _visualize_expression_tree(node.left_child, dot)
    if node.right_child is not None:
        dot.edge(str(id(node)), str(id(node.right_child)))
        _visualize_expression_tree(node.right_child, dot)

expression = '5 + 4 * 3 - 2 / 1'
root = build_expression_tree(expression)
visualize_expression_tree(root)
