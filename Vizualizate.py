from Tree import Tree


def visualize(tree, nest_level):
        for node in tree.nodes:
            if type(node) is Tree:
                i = 1
        while i < nest_level:
            print(" ", end="")
            i += 1
            print(" |--> " + node.name)
            visualize(node, nest_level + 1)
            if type(node) is str:
                i = 1
        while i < nest_level:
            print(" ", end="")
            i += 1
            print(" |--> " + node)