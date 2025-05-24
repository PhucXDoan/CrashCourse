from Hint_003_My_Tokenizer_Implementation import tokenize, SYMBOLS

OPERATORS = '<= >= < > = + - * / ^'.split()

def naive_parser(tokens):

    expr = None

    if tokens:
        match tokens[0]:

            case number if isinstance(number, float):

                expr = number
                del tokens[0]

            case identifier if identifier not in SYMBOLS:
                expr = identifier
                del tokens[0]

            case '-':
                del tokens[0]
                expr = ('-', naive_parser(tokens))

            case '(':

                del tokens[0]

                expr = naive_parser(tokens)

                assert tokens[0] == ')', tokens

                del tokens[0]

            case _:
                raise RuntimeError('Expected expression!')

    if expr is not None and tokens and (operator := tokens[0]) in OPERATORS:
        del tokens[0]
        expr = (expr, operator, naive_parser(tokens))

    return expr

def show_tree(tree):
    match tree:
        case (lhs, op, rhs ): return f'({show_tree(lhs)}{op}{show_tree(rhs)})'
        case (     op, expr): return f'({op}{show_tree(expr)})'
        case value          : return f'{value}'

print(show_tree(naive_parser(tokenize('1 + 1 - 3.14 + (2 * -7) >= val'))))
