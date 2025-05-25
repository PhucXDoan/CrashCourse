# Printing a tree is done using recursion,
# where the function that prints the tree calls itself.
# This is apparent in the fact that trees have trees within themselves.
# The trick to having a good print output is keeping track of how "deep"
# the tree printing is so far, which is done here using the `depth` argument.
#
# Example:
#   > print_tree(((0, '*', 1), '+', (2, '+', ('-', 3))))
#   '+'
#    |  '*'
#    |   |  0
#    |   |
#    |   |  1
#    |
#    |  '+'
#    |   |  2
#    |   |
#    |   |  '-'
#    |   |   |  3

def print_tree(tree, depth=0):

    def print_indented(string):
        nonlocal depth
        print(' |  ' * depth + string)

    match tree:

        # Binary operator.
        case (lhs, op, rhs):
            print_indented(f"'{op}'")
            print_tree(lhs, depth=depth+1)
            print_indented(' |')
            print_tree(rhs, depth=depth+1)

        # Unary operator.
        case (op, expr):
            print_indented(f"'{op}'")
            print_tree(expr, depth=depth+1)

        # Leaf of the AST.
        case value:
            print_indented(str(value))
