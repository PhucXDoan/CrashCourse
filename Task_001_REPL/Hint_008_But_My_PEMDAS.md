# But My PEMDAS!

If we were to use the same pseudo-algorithm as described in the previous hint file
on the string `'3 - 4 + 1 + 0.1 * 7'`,
we end up with the following AST:
```
              '*'
              / \
             /   \
           '+'    7
           / \
          /   \
        '+'   0.1
        / \
       /   \
     '-'    1
     / \
    /   \
   3     4
```

This is not correct[^1],
because we end up doing subtraction and addition first
(bottom of the AST, so they'd be evaluated first)
and the multiplication is done last (root of the tree).

To fix this, we need to first define the precedence
of each operator in our REPL program:
```python
PRECEDENCES = {
    '='  : 4,
    '<'  : 4,
    '>'  : 4,
    '<=' : 4,
    '>=' : 4,

    '+'  : 3,
    '-'  : 3,

    '*'  : 2,
    '/'  : 2,

    '^'  : 1,
}
```

By convention: the lower the number is, the more tightly bounded that operator is.
For instance,
the equality and inequality operators have the highest number in the dictionary,
and as a result,
they'd appear at the top of the AST.
The exponentiation operation (`^`) has the lowest number,
thus is the most bounded (that is, always done first before anything else).

Here's an example of the proper AST for `'1 * 5 ^ 9 + 3 > 5 ^ 10'`
with the precedence of the operators denoted.
Notice how the numbers "flow" from greatest to least down the tree.
```
            '>':4
            / \
           /   \
         '+':3  \
         / \     \
        /   \     \
      '*':2  3     \
      / \           \
     /   \           \
    1    '^':1       '^':1
         / \         / \
        /   \       /   \
       5     9     5     10
```

The only time this wouldn't be the case is if there were parentheses
changing the order of operations;
for instance, when we have `'1 * 5 ^ (9 + 3) > 5 ^ 10'`:
```
         '>':4
         / \
        /   \
      '*':2  \
      / \     \
     /   \     \
    1    '^':1  \
         / \     \
        /   \     \
       5    '+':3  \
            / \     \
           /   \     \
          9     3     \
                      '^':1
                      / \
                     /   \
                    5     10
```

Note that we have only considered binary operators;
there'd be a prescedence table for unary operators (and any other n-ary operators)
too, but small steps at a time!

> **Excercise**: with this knowledge of precedence,
> can you think of a way to tweak the pseudo-algorithm
> to incorporate the order of operations?

[^1]: Technically, there's nothing "wrong" with this.
It is by convention, however,
that mutliplication (and division) is done first
before addition and subtraction.
Likwise, we'd do exponentiation first before multiplication/division.
Mathematics as a whole, however, would not be any different
if this convention was backwards,
or if we did everything left-to-right,
which is how our current pseudo-algorithm is doing it right now;
all that would happen is that we end up needing a lot of parentheses
to enforce the order of operations we want.
