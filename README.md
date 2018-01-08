# HOW TO USE IT?

```python
from lib.main import get_unique_id

# Default returns id with length 14 and without `:*^`\",.~;%+-'` chars.
print(get_unique_id())

# Returns id with length 8 and without `A` and `a` letters.
print(get_unique_id(length="8", excluded_chars="Aa"))
```
