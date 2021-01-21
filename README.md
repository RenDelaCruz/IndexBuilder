# IndexBuilder

This program effortlessly creates an ordered book index simply from entering terms and their corresponding pages.

#

Clone the repository with
```bash
git clone https://github.com/RenDelaCruz/IndexBuilder.git
```

Run `index_builder.py` to start.

#

Simply enter a term and the corresponding pages, or page ranges, separated by commas. Entering the same term will update the entry with the additional pages. To enter 'apple' found on pages 1, 3 and 6-12, type in `apple, 1, 3, 6-12`. All of the term entries are automatically ordered alphabetically, and the pages numerically.


Example index:

```
______________________________

Index

A
apple, 1, 3, 6-12
apricot, 3, 6, 11

O
orange, 2, 6-12

S
seed, 4
______________________________

```

#

TODO

- Add text file saving feature
- Add subentries
