# HOW TO INSTALL?

`pip install unique-id`

# HOW TO USE IT?

To get unique ID you have to call method `get_unique_id`.

```python
from lib.main import get_unique_id

# Default returns id with length 14 and without `:*^`\",.~;%+-'` chars.
my_id = get_unique_id()
print(my_id)

# Returns id with length 8 and without `A` and `a` letters.
my_id = get_unique_id(length="8", excluded_chars="Aa")
print(my_id)
```
