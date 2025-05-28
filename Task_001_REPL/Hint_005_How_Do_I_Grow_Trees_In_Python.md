# How Do I Grow Trees in Python?

We can use tuples where the first and third slot is the LHS and RHS respectively
while the second slot is the token.

Simple example:
```
tree = (1, '+', 2)
```
```
          '+'
          / \
         /   \
        1     2
```

Deeper example:
```
tree = (1, '+', (2, '-', 3))
```
```
          '+'
          / \
         /   \
        1    '-'
              /\
             /  \
            2    3
```

Deepest example:
```
tree = ((0, '*', 1), '+', (2, '-', 3))
```
```
          '+'
          / \
         /   \
       '*'   '-'
       /\     /\
      /  \   /  \
     0    1 2    3
```

What about unary operators?
For something like negation,
we can use the format of `('-', _)`.
```
tree = ((0, '*', 1), '+', (2, '+', ('-', 3)))
```
```
          '+'
          / \
         /   \
       '*'   '+'
       /\     /\
      /  \   /  \
     0    1 2   '-'
                 |
                 |
                 3
```

> **Exercise**: Given a tree like `((0, '*', 1), '+', (2, '+', ('-', 3)))`,
> make a function that can print it out into something more readable.
> It doesn't need to be like the ASCII art above, but an output like:
> ```
> ((0*1)+(2+(-3)))
> ```
> or:
> ```
> '+'
>  | '*'
>  |  | 0
>  |  |
>  |  | 1
>  |
>  | '+'
>  |  | 2
>  |  |
>  |  | '-'
>  |  |  | 3
> ```
> will be very useful for debugging later on.
> Note that this will require **recursion**.
