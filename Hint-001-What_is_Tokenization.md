# What is Tokenization?

Suppose the input string:
```python
given = '3.14 + (2 * -7) >= val'
```

A string is nothing but a list of characters:
```python
chars = [
  '3', '.', '1', '4', ' ',
  '+', ' ', '(', '2', ' ',
  '+', ' ', '-', '7', ')',
  ' ', '>', '=', ' ', 'v',
  'a', 'l',
]
```

We can collect groups of these characters into something called tokens:
```python
tokens = [
  '3.14',
  '+',
  '(',
  '2',
  '*',
  '-',
  '7',
  ')',
  '>=',
  'val',
]
```

This process is called **tokenization**.
If we were to implement our REPL using only the given input string, it'd be a lot of hassle,
because we'd be analyzing the string on a character-by-character basis;
it'd be like reading English letter-by-letter instead of whole words.
By tokenizing `given`, we can massage our input data into something easier to use
(we no longer have to think about whitespace for instance).

Can you implement a Python function that can take a string and return a list of tokens?
The specification of what constitute a token is left up to you to decide,
but if you're unsure,
just focus on getting something working.
You can always adjust your tokenization algorithm later on!
