# What are Abstract Syntax Trees?

An Abstract Syntax Tree (AST) is a data structure that describes
the syntax of a particular expression under some grammar.
Sounds complicated, but it's easy to see how it can be applied
to our REPL program with an example:
```
        '3.14 + (2 * -7) >= val'

                    |
                    v

                  '>='
                   /\
                  /  \
               '+'   'val'
               / \
              /   \
           3.14   '*'
                  / \
                 /   \
                2    '-'
                      |
                      |
                      7
```

The **root** of the tree is the `'>='` token
and there are branches which go to other tokens all the way down.
The tokens that are at the end of the tree (`3.14`, `2`, `7`, and `'val'`)
are what we'd call **leaves**.
This data structure is very useful
because it gives us the ability to pretty much evaluate the expression right here.

We'd begin at the very bottom of the tree at the `7` token;
there's not much else to say about this token since it's just a number,
so we then look at its parent: the `'-'` token.
Since this parent token has only one branch,
we know it's a unary `-` operator (negation),
so we simply negate to get `-7`.
```
                  '>='
                   /\
                  /  \
               '+'   'val'
               / \
              /   \
           3.14   '*'
                  / \
                 /   \
                2    -7
```

We move up again and see the `'*'` token.
This time the parent token has two branches,
which makes sense since this is multiplication.
We go ahead and multiply the LHS and RHS:
```
                  '>='
                   /\
                  /  \
               '+'   'val'
               / \
              /   \
           3.14   -14
```

We pretty much repeat the process again when we move up to the `'+'` token.
```
                  '>='
                   /\
                  /  \
             -10.86  'val'
```

When we move up to the `'>='` token,
it also has two branches,
but rather than a number token this time,
we have an identifier token of `'val'`.
Let's just say the variable `'val'` is already defined somehow and it is equal to `-1`.
We can just substitute it in and get:
```
                  '>='
                   /\
                  /  \
            -10.86    -1
```

Finally, we simply evaluate one last time to finally get:
```
                  False
```

Thus, the expression `'3.14 + (2 * -7) >= val'` should have the REPL program yield `False`.

The structure of the syntax tree is important
because it naturally encodes the operator precedence of the original expression.
Consider the ASTs for the two following expressions:
```
               '1 - 2 * 3'

                    |
                    v

                   '-'
                   /\
                  /  \
                 1   '*'
                      /\
                     /  \
                    2    3
```
```
             '(1 - 2) * 3'

                    |
                    v

                   '*'
                   /\
                  /  \
                '-'   3
                /\
               /  \
              1    2
```

> **Exercise**: create some mathematical expressions (e.g. `'1 + 2 * (3 + 4 * (5 + ...))'`)
> and draw out the trees for it.
> Get some intution for how the code that'd make the AST might look.

If we can create an AST from tokens,
we'd no longer need parentheses to denote the order of how to evaluate the operators
(just like tokenization removes us from having to worry about whitespace).
However, that begs the question: how do we create such a tree?

But before that, think about how we might implement
a tree data structure in Python first.
