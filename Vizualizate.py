from Tree import Tree


def visualize(tree, nest_level):
    if type(tree) is Tree:
        i = 1
        while i < nest_level:
            print(" ", end="")
            i += 1
        if len(tree.nodes) == 0:
            # tree.name = "<empty>"
            print(" |--> <empty>")
        else:
            print(" |--> " + tree.name)
            for node in tree.nodes:
                visualize(node, nest_level + 1)
    else:
        i = 1
        while i < nest_level:
            print(" ", end="")
            i += 1
        print(" |--> " + str(tree))

