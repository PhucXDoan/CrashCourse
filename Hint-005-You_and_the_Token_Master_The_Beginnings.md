# You and the Token-Master: The Beginnings.

To learn how to create an AST from a list of tokens,
let's look at a simple example
and see if we (the humans) can do it just from intution.
To do this, let's imagine a scene between two characters:
the Token-Master and you.
The Token-Master is the one with the list of tokens
but will only reveal to you one token at a time.
Your mission will then be to build a AST based on what the Token-Master is telling you.

>   (**You**) What is the first token, Token-Master?
>
>   (**Token-Master**) It is a `'3'`.
>
>   (**You**) Okay, so a number.
>   It's likely this number is part of a bigger expression, though.
>   What's the next token then, Token-Master?
>
>   (**Token-Master**) It is a `'-'`.
>
>   (**You**) Aha, a minus sign!
>   Thus, we can expect our AST to have something like this:
>   ```
>            '-'
>            /\
>           /  \
>         '3'  ???
>   ```
>   I've seen the LHS of the `'-'` (that being the `'3'` token),
>   but I now need to figure out the RHS.
>   So, Token-Master, what is the next token?
>
>   (**Token-Master**) It is a `'4'`.
>
>   (**You**) Sweet, it's just another number token!
>   This just means I have the following AST:
>   ```
>            '-'
>            /\
>           /  \
>         '3'  '4'
>   ```
>
>   (**Token-Master**) You still have tokens left.
>
>   (**You**) Right, so what is it?
>
>   (**Token-Master**) The next token is `'+'`.
>
>   (**You**) Okay, another operator token.
>   This one is just addition, so I can just slap this on top of the AST so far:
>   ```
>               '+'
>               /\
>              /  \
>            '-'  ???
>            /\
>           /  \
>         '3'  '4'
>   ```
>   We just need to find the RHS of the `'+'` now.
>   What's next, Token-Master?
>
>   (**Token-Master**) The next token is `'1'`.
>
>   (**You**) That leaves me with the new AST:
>   ```
>               '+'
>               /\
>              /  \
>            '-'  '1'
>            /\
>           /  \
>         '3'  '4'
>   ```
>   This seems pretty easy.
>   Is there anything left, Token-Master?
>
>   (**Token-Master**) The next token is `'+'`.
>
>   (**You**) No problem:
>   ```
>                 '+'
>                 /\
>                /  \
>               '+'  ???
>               /\
>              /  \
>            '-'  '1'
>            /\
>           /  \
>         '3'  '4'
>   ```
>   What's next?
>
>   (**Token-Master**) The next token is `'('`.
>
>   (**You**) Ah, something more interesting now!
>   This opening parenthesis means we have a subexpression coming up,
>   so let's start a new AST and put the old AST somewhere else for now.
>   What's the next token, Token-Master?
>
>   (**Token-Master**) The next token is `'0.1'`.
>
>   (**You**) ... and the one after that?
>
>   (**Token-Master**) It is a `'\*'`.
>
>   (**You**) Alright, so this subexpression's tree so far looks like:
>   ```
>                   '\*'
>                   /\
>                  /  \
>               '0.1' ???
>   ```
>   What's next, Token-Master?
>
>   (**Token-Master**) It is a `'7'`.
>
>   (**You**) Cool, this gives us:
>   ```
>                   '\*'
>                   /\
>                  /  \
>               '0.1' '7'
>   ```
>   Next!
>
>   (**Token-Master**) It is a `')'`.
>
>   (**You**) I see; this is the end of the sub-expression then.
>   I'll just insert the new AST right into the RHS of the old AST to get one big tree:
>   ```
>                  '+'
>                  /\
>                 /  \
>               '+'   \
>               /\     \
>              /  \     \
>            '-'  '1'   '\*'
>            /\          /\
>           /  \        /  \
>         '3'  '4'  '0.1'  '7'
>   ```
>   Looks nice!
>   I think I get the hang of this now.
>   Is there anything left, Token-Master?
>
>   (**Token-Master**) Nope.
>
>   (**You**) Yippee! I have finished building the AST!
