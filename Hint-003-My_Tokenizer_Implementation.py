# Example:
#   > print(tokenize('3.14 + (2 * -7) >= val'))
#   ['3.14', '+', '(', '2', '*', '-', '7', ')', '>=', 'val']
#
# Potential improvements:
#   - Better error messages (e.g. print out the string
#       and point to where it failed to tokenize).
#   - Validation of number tokens (e.g. no multiple decimal points).
#   - More complicated number tokens (e.g. imaginary numbers
#       like "3i" being a single token).
#   - Allow apostrophes in identifiers, but only at the end
#       (like f' being the derivative of f).

NUMBER_CHARACTERS     = '0123456789.'
IDENTIFIER_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def tokenize(string):

        tokens = []

        while string: # Grab tokens until we've processed the entire string.

            # Ignore whitespace.
            if string[0].isspace():
                string = string[1:]

            # Number token.
            elif string[0] in NUMBER_CHARACTERS:

                token = ''

                while string and string[0] in NUMBER_CHARACTERS:
                    token  += string[0 ]
                    string  = string[1:]

                tokens += [token]

            # Identifier token.
            elif string[0] in IDENTIFIER_CHARACTERS:

                token = ''

                while string and string[0] in IDENTIFIER_CHARACTERS:
                    token  += string[0 ]
                    string  = string[1:]

                tokens += [token]

            # Symbol token.
            elif symbols := [x for x in [
                '<=', '>=', '<', '>', '=',
                '+', '-', '*', '/', '^',
                '(', ')',
            ] if string.startswith(x)]:

                # There might be multiple matches, like "<=" and "<",
                # so we pick the one that'd be the longest.
                # `max` can do this; if you give `max` a list of numbers,
                # it'd give the largest number. However, we have a list of strings,
                # so we tell `max` to use the function `len` to get the string's length
                # and get the string with the longest length.
                token = max(symbols, key=len)

                tokens += [token]
                string  = string[len(token):]

            # Unknown token; a better diagnostic could be done here.
            else:
                raise RuntimeError('Unknown token!')

        return tokens
