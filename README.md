# Introduction:
This is a small python module to design a singleton class python (will add more later on).I have been using python for 2 years and fell in love with it and I would really love to give something (even as small as this module) to the community. If you like it give it a start,hate it tell me why I will try to fix it and you could help too.

## Design Patterns Supported
> Singleton

# Example

```python

from design_patterns import singleton
@singleton
class HelloWorld:
    def __init__(self):
        self.name = "one instance"


h = HelloWorld()
r = HelloWorld()

if __name__ == "__main__":
    print(r == h)
  
```
