# What are Abstract Syntax Trees?

An Abstract Syntax Tree (AST) is a data structure that describes
the syntax of a particular expression under some grammar.
Sounds complicated, but it's easy to see how it can be applied
to our REPL program with an example:
```
        "3.14 + (2 * -7) >= val"

                    |
                    v

                  ">="
                   /\
                  /  \
               "+"    "val"
               / \
              /   \
        "3.14"    "*"
                  / \
                 /   \
               "2"   "-"
                      |
                      |
                     "7"
```

The **root** of the tree is the `">="` token
and there are branches which go to other tokens.
The tokens that are at the end of the tree (`"3.14"`, `"2"`, `"7"`, and `"val"`)
are what we'd call **leaves**. This data structure is very useful
because it gives us the ability to pretty much evaluate the expression right here.

We'd begin at the very bottom of the tree at the `"7"` token,
which we'd parse as the number `7`.
```
                  ">="
                   /\
                  /  \
               "+"    "val"
               / \
              /   \
        "3.14"    "*"
                  / \
                 /   \
               "2"   "-"
                      |
                      |
                      7
```

We then move up and see the `"-"` token.
Since this token has only one branch,
we know it's a unary `-` operator,
so we simply negate the value we have so far to get `-7`.
```
                  ">="
                   /\
                  /  \
               "+"    "val"
               / \
              /   \
        "3.14"    "*"
                  / \
                 /   \
               "2"   -7
```

We move up again and see the `"*"` token.
This token has two branches,
and we have only evaluated one of them (the `-7`),
so we need to evaluate the other branch too.
The other branch is just a `"2"` which parses as `2`.
```
                  ">="
                   /\
                  /  \
               "+"    "val"
               / \
              /   \
        "3.14"    "*"
                  / \
                 /   \
                2    -7
```

Now we can actually perform the multiplication.
```
                  ">="
                   /\
                  /  \
               "+"    "val"
               / \
              /   \
        "3.14"    -14
```

We pretty much repeat the process again when we move up to the `"+"` token.
```
                  ">="
                   /\
                  /  \
            -10.86    "val"
```

When we move up to the `">="` token, it also has two branches that need to all be
evaluated (just like before with `"+"` and `"*"`).
Rather than a number token this time, however, we have an identifier token of `"val"`.
Let's just say the variable `"val"` is already defined and it is equal to `-1`.
```
                  ">="
                   /\
                  /  \
            -10.86    -1
```

Finally, we simply evaluate one last time to finally get:
```
                  False
```

Thus, the expression `"3.14 + (2 * -7) >= val"` should have the REPL program yield `False`.

The structure of the syntax tree is important
because it essentially encodes the operator precedence of the original expression.
Consider the ASTs for the two following expressions:
```
               "1 - 2 * 3"

                    |
                    v

                   "-"
                   /\
                  /  \
                 1   "*"
                      /\
                     /  \
                    2    3
```
```
             "(1 - 2) * 3"

                    |
                    v

                   "*"
                   /\
                  /  \
                "-"   3
                /\
               /  \
              1    2
```

If we can create an AST from tokens,
we'd no longer need parentheses to denote the order of how to evaluate the operators
(just like tokenization removes us from having to worry about whitespace).

However, the question is now: how do we create such a tree?

Excercise: create some mathematical expressions (e.g. `"1 + 2 * (3 + 4 * (5 + ...))"`)
and see if you can come up with a set of pseudo-algorithm on how to make a AST from it.
