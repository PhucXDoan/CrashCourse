# How Do I Tokenize?

Suppose the input string:
```python
given = '3.14 + (2 * -7) >= val'
```

To get the first token, we'd examine the first character.
We see the digit `'3'`, so this means we should be looking for a "number token".
We then look at the next few characters
until we encounter the first character
that shouldn't make up the number token (e.g whitespace).
```
given = '3.14 + (2 * -7) >= val'
         ^^^^*
         |   |
         |   End of the number.
         |
  Should be grouped together.
```

Thus we should make a token that is `3.14` and then store it in a list.

We can then advance the given input string to be where we stopped:
```python
given  = ' + (2 * -7) >= val'
tokens = [3.14]
```

From here on out, we simply repeat the process to get the next token.

The first character is now whitespace, however, so we'll just cut it out:
```python
given  = '+ (2 * -7) >= val'
tokens = [3.14]
```

The first character is now `'+'`.
This is a standalone token, so we can just pop it and put it in the list of tokens.
```python
given  = ' (2 * -7) >= val'
tokens = [3.14, '+']
```

The first character now is another whitespace,
but it's the same thing: cut it and move on.
Let's fast-forward tokenization process a bit:
```python
given  = '>= val'
tokens = [3.14, '+', '(', 2, '*', '-', 7]
```

Notice that we have two tokens, `'-'` and `7`, rather than a single number token of `-7`.
I've chosen to make our hypothetical tokenizer behave like this,
but you can *try*[^1] to make it where if it sees a `'-'`,
it checks if there's a digit immediately after.
If so, then this is a negative sign of the number, so it should emit the token for `-7`.

[^1]: However, I suggest you don't do this, because it actually makes parsing the input string more difficult.
If we were tokenizing `'2 - 3'`, then really we should end up with `[2, '-', 3]` and not `[2, -3]`
since the `-` is the subtraction operator.
On the other hand, if we instead have `'2 - - 3'`,
then the list of tokens would be `[2, '-', -3]` now.
This means whether or not the `-` ends up being a part of the number token depends a lot on the context,
making your implementation of the tokenizer more complicated.
None of this is necessary if you always interpret `-` as its own separate token,
since we can resolve all of these issues once we build a syntax tree (hint!).

Another thing to note is the token `'>='`;
the tokenizer should recognize that this is one single token
and not a `'>'` token followed by a `'='` token.[^2]

The final token list ends up being:
```python
tokens = [3.14, '+', '(', 2, '*', '-', 7, '>=', 'val']
```
where the `'val'` token can be thought as some sort of variable
(which I'll generically use the term "identifier").

[^2]: What if you have an input like `'1 < = 2'`?
Should the token list be `[1, '<', '=', 2]` or `[1, '<=', 2]`?
That's up to you to decide.

Once you roughly understand these tiny details,
you'll see that the tokenization process is really that simple.
Additional things can be done to further improve your implementation of the tokenizer,
such as validating the form of numbers (e.g. cannot contain multiple decimal points),
or having more complicated tokens (e.g. hexadecimal literals like `0xD28F`
or scientific notation like `837e-3` which is interpreted as 837\*10^-3).
