# You and the Token-Master: The Sequel.

Note: this scene is quite dense, so take your time digesting it.

>   (**You**) What is the first token, Token-Master?
>
>   (**Token-Master**) It is a `1`.
>
>   (**You**) Okay, so a number like the first time around.
>   What's the next token then, Token-Master?
>
>   (**Token-Master**) It is a `'+'`.
>
>   (**You**) A plus sign, and like before, the AST might look something like:
>   ```
>            '+':3
>            / \
>           /   \
>          1    ???
>   ```
>   What's next, Token-Master?
>
>   (**Token-Master**) The next token is a `2`.
>
>   (**You**) Now, the naive thing to think
>   would be that the AST should now look like:
>   ```
>            '+':3
>            / \
>           /   \
>          1     2 (naively)
>   ```
>   ... but this might not be right,
>   because if the next token is something like `'*'`,
>   then the tree would actually be:
>   ```
>            '+':3
>            / \
>           /   \
>          1    '*':2 (hypothetically)
>               / \
>              /   \
>             2    ???
>   ```
>   To figure this out,
>   let's stash the AST away for now and keep the `2` token separate.
>   ```
>            (A)     |    (B)
>            '+':3   |     2
>            / \     |
>           /   \    |
>          1    ???  |
>   ```
>   What's the next token, Token-Master?
>
>   (**Token-Master**) It is a `'/'`.
>
>   (**You**) So it looks like I was right!
>   It isn't the `'*'` token,
>   but the effect is the same anyways because division
>   has a tighter precedence than addition.
>   We can make the second AST like so:
>   ```
>            (A)     |    (B)
>            '+':3   |    '/':2
>            / \     |    / \
>           /   \    |   /   \
>          1    ???  |  2    ???
>   ```
>   Let's now look at the next token, Token-Master!
>
>   (**Token-Master**) It is a `9`.
>
>   (**You**) I have to be careful again;
>   I can't just put `9` in tree (B) because of the same reason as before
>   (if the next token is something like `'^'`).
>   So once again, I'm going to start a new tree with the root being the `9` token.
>   ```
>            (A)     |    (B)     |    (C)
>            '+':3   |    '/':2   |     9
>            / \     |    / \     |
>           /   \    |   /   \    |
>          1    ???  |  2    ???  |
>   ```
>   Give it, Token-Master!
>
>   (**Token-Master**) The next token is a `'-'`.
>
>   (**You**) Ah, so we're back to the level of `'+'` and `'-'`.
>   What this mean then is that we should probably merge trees (B) and (C)
>   to get something that looks like `(2/9)`:
>   ```
>            (A)     |    (B)
>            '+':3   |    '/':2
>            / \     |    / \
>           /   \    |   /   \
>          1    ???  |  2     9
>   ```
>   we might as well merge (A) and (B) to get something like `(1+(2/9))`:
>   ```
>            (A)
>            '+':3
>            / \
>           /   \
>          1   '/':2
>              / \
>             /   \
>            2     9
>   ```
>   We can then put the `'-'` at the top to
>   resemble something like `((1+(2/9))-(???))`:
>   ```
>           (A)
>           '-':3
>           / \
>          /   \
>        '+':3 ???
>        / \
>       /   \
>      1   '/':2
>          / \
>         /   \
>        2     9
>   ```
>   All of this merging stuff is a bit complicated,
>   I'm just working it out based on intution,
>   but what I have right now does correspond
>   to `1+2/9-???` done in the proper order of operations...
>   Let's just keep going; what's next, Token-Master?
>
>   (**Token-Master**) The next token is a `5`.
>
>   (**You**) Okay, let's make another tree again like before:
>   ```
>           (A)     |    (B)
>           '-':3   |     5
>           / \     |
>          /   \    |
>        '+':3 ???  |
>        / \        |
>       /   \       |
>      1   '/':2    |
>          / \      |
>         /   \     |
>        2     9    |
>   ```
>   Next, Token-Master?
>
>   (**Token-Master**) The next token is a `'-'`.
>
>   (**You**) I have to be careful again,
>   because if I were to put the `'-'` token in tree (B),
>   then I'd have:
>   ```
>           (A)     |    (B)
>           '-':3   |    '-':3 (naively)
>           / \     |    / \
>          /   \    |   5  ???
>        '+':3 ???  |
>        / \        |
>       /   \       |
>      1   '/':2    |
>          / \      |
>         /   \     |
>        2     9    |
>   ```
>   ... but this would mean something like `'1 - 2 - 3'`
>   ends up being `'(1 - (2 - 3))'` and not `'((1 - 2) - 3)'`![^1]
>   What I should do instead is is merge (A) and (B)
>   and then put the `'-'` at the top:
>   ```
>              (A)
>              '-':3
>              / \
>             /   \
>           '-':3 ???
>           / \
>          /   \
>        '+':3  5 <- This was (B).
>        / \
>       /   \
>      1   '/':2
>          / \
>         /   \
>        2     9
>   ```
>   Whew... What's next, Token-Master?
>
>   (**Token-Master**) The next token is a `0`.
>
>   (**You**) Same routine:
>   ```
>              (A)     |     (B)
>              '-':3   |      0
>              / \     |
>             /   \    |
>           '-':3 ???  |
>           / \        |
>          /   \       |
>        '+':3  5      |
>        / \           |
>       /   \          |
>      1   '/':2       |
>          / \         |
>         /   \        |
>        2     9       |
>   ```
>   Next!
>
>   (**Token-Master**) The next token is a `'^'`.
>
>   (**You**) This time we do put the operator in tree (B)
>   instead of merging it with (A);
>   intuitively, this is because `'^'` has tighter precedence than `'-'`.
>   ```
>              (A)     |     (B)
>              '-':3   |     '^':1
>              / \     |     / \
>             /   \    |    /   \
>           '-':3 ???  |   0    ???
>           / \        |
>          /   \       |
>        '+':3  5      |
>        / \           |
>       /   \          |
>      1   '/':2       |
>          / \         |
>         /   \        |
>        2     9       |
>   ```
>   Gimme, gimme, Token-Master!
>
>   (**Token-Master**) The next token is a `7`.
>
>   (**You**) Out of habit, let's make another tree again:
>   ```
>              (A)     |     (B)     |     (C)
>              '-':3   |     '^':1   |      7
>              / \     |     / \     |
>             /   \    |    /   \    |
>           '-':3 ???  |   0    ???  |
>           / \        |             |
>          /   \       |             |
>        '+':3  5      |             |
>        / \           |             |
>       /   \          |             |
>      1   '/':2       |             |
>          / \         |             |
>         /   \        |             |
>        2     9       |             |
>   ```
>   What's new, Token-Master?
>
>   (**Token-Master**) That was the last token.
>
>   (**You**) Alright, then we should merge everything together;
>   here's (B) and (C) merged:
>   ```
>              (A)     |     (B)
>              '-':3   |     '^':1
>              / \     |     / \
>             /   \    |    /   \
>           '-':3 ???  |   0     7
>           / \        |
>          /   \       |
>        '+':3  5      |
>        / \           |
>       /   \          |
>      1   '/':2       |
>          / \         |
>         /   \        |
>        2     9       |
>   ```
>   ... then (A) and (B):
>   ```
>              '-':3
>              / \
>             /   \
>           '-':3  \
>           / \     \
>          /   \     \
>        '+':3  5    '^':1
>        / \         / \
>       /   \       /   \
>      1   '/':2   0     7
>          / \
>         /   \
>        2     9
>   ```
>   Because that was the last token,
>   the input string must've looked something like `'1 + 2 / 9 - 5 - 0 ^ 7'`.
>   Furthermore, I didn't encounter any parentheses,
>   so I know for a fact that all of the operator's precedences
>   should be in decreasing order starting from the root,
>   which is indeed what I see in the tree I made.

That was a lot,
and you probably have a lot of questions like when exactly new trees should be
made or when should they be merged,
or how are we going to handle unary operators and such;
but don't worry,
this is by no mean a simple algorithm,
we'll just have to look at a lot more examples
to get more comfortable with properly making ASTs.

The next hint file will be another example of parsing
(like the one we just went through).

[^1]: What we want is called **left-associativity**.
