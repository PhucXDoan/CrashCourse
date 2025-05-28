# Big Parsing Example

---

> `1 + 2 * 3^2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The first token is a `1`, so:
```
           (A)
            1
```

---

> `+ 2 * 3^2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `'+'` with a precedence of 3;
there's no other tree we have to think about merging
or whatever, so we can just append this operator to
our current tree:
```
           (A)
           '+':3
           / \
          /   \
         1    ???
```

---

> `2 * 3^2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `2`;
we make a new AST with that as the root:
```
           (A)     |    (B)
           '+':3   |     2
           / \     |
          /   \    |
         1    ???  |
```

---

> `* 3^2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `'*'` with a precedence of 2;
the previous tree has an `'+'` operator at the root
with precedence of 3. Since the `'*'` has tighter
precedence than `'+'`, we should not merge the trees!
Let's put the `'*'` operator into tree (B):
```
           (A)     |    (B)
           '+':3   |    '*':2
           / \     |    / \
          /   \    |   /   \
         1    ???  |  2    ???
```

---

> `3^2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `3`;
once more, we make a new tree:
```
           (A)     |    (B)     |    (C)
           '+':3   |    '*':2   |     3
           / \     |    / \     |
          /   \    |   /   \    |
         1    ???  |  2    ???  |
```

---

> `^2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `'^'` with precedence of 1;
this also has a tighter precedence than `'*'`,
so we won't merge yet.
```
           (A)     |    (B)     |    (C)
           '+':3   |    '*':2   |    '^':1
           / \     |    / \     |    / \
          /   \    |   /   \    |   /   \
         1    ???  |  2    ???  |  3    ???
```

---

> `2 / 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `2`;
another tree, another day:
```
           (A)     |    (B)     |    (C)    |    (D)
           '+':3   |    '*':2   |    '^':1  |     2
           / \     |    / \     |    / \    |
          /   \    |   /   \    |   /   \   |
         1    ???  |  2    ???  |  3    ??? |
```

---

> `/ 4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `/` with precedence of 2;
this time the operator we're looking at has a weaker
precedence than the previous tree (with the `'^'`).
What we should do then is merge the most recent two
trees we have so far:
```
           (A)     |    (B)     |    (C)
           '+':3   |    '*':2   |    '^':1
           / \     |    / \     |    / \
          /   \    |   /   \    |   /   \
         1    ???  |  2    ???  |  3     2
```
We repeat the process again,
that is, comparing the precedence of the
previous tree (which is now tree (B) with
the operator `'*'`) and our current operator of `'/'`.
These two operators have the same precedence,
but because we want left-associativity,
we'll merge trees (B) and (C):
```
           (A)     |    (B)
           '+':3   |    '*':2
           / \     |    / \
          /   \    |   /   \
         1    ???  |  2    '^':1
                   |       / \
                   |      /   \
                   |     3     2
```
We'd repeat the process once more,
that is, now comparing the precedence of the previous
tree (which is now tree (A) with the operator `'+'`)
and our current operator of `'/'`.
The `'/'` operator has a tigher precedence than `'+'`,
so we stop merging here and put `'/'` in our most
recent tree we have so far:
```
           (A)     |       (B)
           '+':3   |       '/':2
           / \     |       / \
          /   \    |      /   \
         1    ???  |    '*':2 ???
                   |    / \
                   |   /   \
                   |  2    '^':1
                   |       / \
                   |      /   \
                   |     3     2
```
We can now finally move on!

---

> `4 - 10^2 >= 1 * 2 * 3 * 4`

The next token is a `4`;
new tree:
```
           (A)     |       (B)     |     (C)
           '+':3   |       '/':2   |      4
           / \     |       / \     |
          /   \    |      /   \    |
         1    ???  |    '*':2 ???  |
                   |    / \        |
                   |   /   \       |
                   |  2    '^':1   |
                   |       / \     |
                   |      /   \    |
                   |     3     2   |
```

---

> `- 10^2 >= 1 * 2 * 3 * 4`

The next token is a `'-'` with precedence of 3;
this operator has a weaker precedence than
the previous tree's operator of `'/'`, so we merge
trees (B) and (C):
```
           (A)     |       (B)
           '+':3   |       '/':2
           / \     |       / \
          /   \    |      /   \
         1    ???  |    '*':2  4
                   |    / \
                   |   /   \
                   |  2    '^':1
                   |       / \
                   |      /   \
                   |     3     2
```
... the previous tree now has an operator of `'+'`
which is on the same precedenc level as `'-'`.
With the same reasoning as before where we want
left-associativity, we do another merge:
```
           (A)
           '+':3
           / \
          /   \
         1   '/':2
             / \
            /   \
          '*':2  4
          / \
         /   \
        2    '^':1
             / \
            /   \
           3     2
```
We now attach the `'-'` token:
```
           (A)
           '-':3
           / \
          /   \
        '+':3 ???
        / \
       /   \
      1   '/':2
          / \
         /   \
       '*':2  4
       / \
      /   \
     2    '^':1
          / \
         /   \
        3     2
```
Looking good so far!

---

> `10^2 >= 1 * 2 * 3 * 4`

The next token is a `10`;
more trees:
```
           (A)    |    (B)
           '-':3  |     10
           / \    |
          /   \   |
        '+':3 ??? |
        / \       |
       /   \      |
      1   '/':2   |
          / \     |
         /   \    |
       '*':2  4   |
       / \        |
      /   \       |
     2    '^':1   |
          / \     |
         /   \    |
        3     2   |
```

---

> `^2 >= 1 * 2 * 3 * 4`

The next token is a `'^'` with precedence of 1;
this is tighter than the previous tree's `'-'`,
so no merging:
```
           (A)    |    (B)
           '-':3  |    '^':1
           / \    |    / \
          /   \   |   /   \
        '+':3 ??? |  10   ???
        / \       |
       /   \      |
      1   '/':2   |
          / \     |
         /   \    |
       '*':2  4   |
       / \        |
      /   \       |
     2    '^':1   |
          / \     |
         /   \    |
        3     2   |
```

---

> `2 >= 1 * 2 * 3 * 4`

The next token is a `2`.
Guess what? More trees!
```
           (A)    |    (B)     |     (C)
           '-':3  |    '^':1   |      2
           / \    |    / \     |
          /   \   |   /   \    |
        '+':3 ??? |  10   ???  |
        / \       |            |
       /   \      |            |
      1   '/':2   |            |
          / \     |            |
         /   \    |            |
       '*':2  4   |            |
       / \        |            |
      /   \       |            |
     2    '^':1   |            |
          / \     |            |
         /   \    |            |
        3     2   |            |
```

---

> `>= 1 * 2 * 3 * 4`

The next token is a `'>='` which has precedence of 4.
This is weaker than `'^'`, so we merge:
```
           (A)    |    (B)
           '-':3  |    '^':1
           / \    |    / \
          /   \   |   /   \
        '+':3 ??? |  10    2
        / \       |
       /   \      |
      1   '/':2   |
          / \     |
         /   \    |
       '*':2  4   |
       / \        |
      /   \       |
     2    '^':1   |
          / \     |
         /   \    |
        3     2   |
```
The operator `'>='` is still weaker than `'-'`,
so we merge again:
```
           (A)
           '-':3
           / \
          /   \
        '+':3  \
        / \     \
       /   \     \
      1   '/':2   \
          / \      \
         /   \      \
       '*':2  4     '^':1
       / \          / \
      /   \        /   \
     2    '^':1   10    2
          / \
         /   \
        3     2
```
We can now put the `'>='` at the root:
```
           (A)
          '>=':4
          /  \
         /    \
       '-':3  ???
       / \
      /   \
    '+':3  \
    / \     \
   /   \     \
  1   '/':2   \
      / \      \
     /   \      \
   '*':2  4     '^':1
   / \          / \
  /   \        /   \
 2    '^':1   10    2
      / \
     /   \
    3     2
```
Hopefully this process is starting to look less scary
to you.

---

> `1 * 2 * 3 * 4`

The next token is a `1`.
They call something along the lines of a "tree-lover":
```
           (A)            |    (B)
          '>=':4          |     1
          /  \            |
         /    \           |
       '-':3  ???         |
       / \                |
      /   \               |
    '+':3  \              |
    / \     \             |
   /   \     \            |
  1   '/':2   \           |
      / \      \          |
     /   \      \         |
   '*':2  4     '^':1     |
   / \          / \       |
  /   \        /   \      |
 2    '^':1   10    2     |
      / \                 |
     /   \                |
    3     2               |
```

---

> `* 2 * 3 * 4`

The next token is a `'*'`.
This has tighter precedence than the previous tree's
`'>='`, so no merging yet:
```
           (A)            |    (B)
          '>=':4          |    '*':2
          /  \            |    / \
         /    \           |   /   \
       '-':3  ???         |  1    ???
       / \                |
      /   \               |
    '+':3  \              |
    / \     \             |
   /   \     \            |
  1   '/':2   \           |
      / \      \          |
     /   \      \         |
   '*':2  4     '^':1     |
   / \          / \       |
  /   \        /   \      |
 2    '^':1   10    2     |
      / \                 |
     /   \                |
    3     2               |
```

---

> `2 * 3 * 4`

The next token is a `2`.
Do you like trees?
```
           (A)            |    (B)     |    (C)
          '>=':4          |    '*':2   |     2
          /  \            |    / \     |
         /    \           |   /   \    |
       '-':3  ???         |  1    ???  |
       / \                |            |
      /   \               |            |
    '+':3  \              |            |
    / \     \             |            |
   /   \     \            |            |
  1   '/':2   \           |            |
      / \      \          |            |
     /   \      \         |            |
   '*':2  4     '^':1     |            |
   / \          / \       |            |
  /   \        /   \      |            |
 2    '^':1   10    2     |            |
      / \                 |            |
     /   \                |            |
    3     2               |            |
```

---

> `* 3 * 4`

The next token is another `'*'`.
Hopefully you get the gist of the process now
and understand why we'd first merge
trees (B) and (C) and then put the new
`'*'` at the top:
```
           (A)            |       (B)
          '>=':4          |       '*':2
          /  \            |       / \
         /    \           |      /   \
       '-':3  ???         |    '*':2 ???
       / \                |    / \
      /   \               |   /   \
    '+':3  \              |  1     2
    / \     \             |
   /   \     \            |
  1   '/':2   \           |
      / \      \          |
     /   \      \         |
   '*':2  4     '^':1     |
   / \          / \       |
  /   \        /   \      |
 2    '^':1   10    2     |
      / \                 |
     /   \                |
    3     2               |
```

---

> `3 * 4`

The next token is a `3`.
More, more, more ASTs:
```
           (A)            |       (B)     |    (C)
          '>=':4          |       '*':2   |     3
          /  \            |       / \     |
         /    \           |      /   \    |
       '-':3  ???         |    '*':2 ???  |
       / \                |    / \        |
      /   \               |   /   \       |
    '+':3  \              |  1     2      |
    / \     \             |
   /   \     \            |
  1   '/':2   \           |
      / \      \          |
     /   \      \         |
   '*':2  4     '^':1     |
   / \          / \       |
  /   \        /   \      |
 2    '^':1   10    2     |
      / \                 |
     /   \                |
    3     2               |
```

---

> `* 4`

The next token is a `'*'`;
you should be comfortable with the next step here:
```
           (A)            |          (B)
          '>=':4          |          '*':2
          /  \            |          / \
         /    \           |         /   \
       '-':3  ???         |       '*':2 ???
       / \                |       / \
      /   \               |      /   \
    '+':3  \              |    '*':2  3
    / \     \             |    / \
   /   \     \            |   /   \
  1   '/':2   \           |  1     2
      / \      \          |
     /   \      \         |
   '*':2  4     '^':1     |
   / \          / \       |
  /   \        /   \      |
 2    '^':1   10    2     |
      / \                 |
     /   \                |
    3     2               |
```

---

> `4`

The final token is a `4`;
out of completeness, let's make one last AST:
```
           (A)            |          (B)     |    (C)
          '>=':4          |          '*':2   |     4
          /  \            |          / \     |
         /    \           |         /   \    |
       '-':3  ???         |       '*':2 ???  |
       / \                |       / \        |
      /   \               |      /   \       |
    '+':3  \              |    '*':2  3      |
    / \     \             |    / \           |
   /   \     \            |   /   \          |
  1   '/':2   \           |  1     2         |
      / \      \          |                  |
     /   \      \         |                  |
   '*':2  4     '^':1     |                  |
   / \          / \       |                  |
  /   \        /   \      |                  |
 2    '^':1   10    2     |                  |
      / \                 |                  |
     /   \                |                  |
    3     2               |                  |
```

---

> ``

There are no tokens left,
so at this point, we begin merging everything!
Here's (B) and (C):
```
           (A)            |          (B)
          '>=':4          |          '*':2
          /  \            |          / \
         /    \           |         /   \
       '-':3  ???         |       '*':2  4
       / \                |       / \
      /   \               |      /   \
    '+':3  \              |    '*':2  3
    / \     \             |    / \
   /   \     \            |   /   \
  1   '/':2   \           |  1     2
      / \      \          |
     /   \      \         |
   '*':2  4     '^':1     |
   / \          / \       |
  /   \        /   \      |
 2    '^':1   10    2     |
      / \                 |
     /   \                |
    3     2               |
```
... and then (A) and (B):
```
                   '>=':4
                   /   \
                  /     \
                 /       \
                /         \
               /           \
              /             \
             /               \
            /                 \
           /                   \
          /                     \
         /                       \
       '-':3                     '*':2
       / \                       / \
      /   \                     /   \
    '+':3  \                  '*':2  4
    / \     \                 / \
   /   \     \               /   \
  1   '/':2   \            '*':2  3
      / \      \           / \
     /   \      \         /   \
   '*':2  4     '^':1    1     2
   / \          / \
  /   \        /   \
 2    '^':1   10    2
      / \
     /   \
    3     2
```
Whew!

---

That was a lot, but hopefully this whole parsing
process doesn't seem too bad now, at least in terms
of intuiting what the next step should be.

Actually implementing this in code is an
entirely different thing, however,
so spend some time brainstorming
how you might turn what we have done here
into a Python program.
