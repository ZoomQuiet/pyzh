# Introduction #



# Suggest Reading #

http://python.net/~goodger/projects/pycon/2007/idiomatic/presentation.html

# Details #
  * Packages
```
package/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py
```


  * Module Structure
```
"""module docstring"""

# imports
# constants
# exception classes
# interface functions
# classes
# internal functions & classes

def main(...):
    ...

if __name__ == '__main__':
    status = main()
    sys.exit(status)
```


  * Import
    1. Good
```
import module
module.name

import long_module_name as mod
mod.name

from module import name
name
```
    1. Bad
```
from module import *
```


  * White Space
    1. **4 spaces** per indentation level.
    1. No hard tabs.
    1. Never mix tabs and spaces.
    1. One blank line between functions.
    1. Two blank lines between classes.
    1. Add a space after "," in dicts, lists, tuples, & argument lists, and after ":" in dicts, but not before.
    1. Put spaces around assignments & comparisons (except in argument lists).
      * Good
```
a = 1
a == b
```
      * Bad
```
a=1
a==b
```
    1. No spaces just inside parentheses or just before argument lists.
    1. No spaces just inside docstrings.


  * Naming
| **type** | **suggest convention** | **example** |
|:---------|:-----------------------|:------------|
| functions, methods | joined\_lower | `say_hello()` |
| constants | ALL\_CAPS | `MONDAY` |
| classes | `StudlyCaps` | `CanlendarConverter` |
| attributes | underline plus attribute name | `_name` |


  * Compound Statements : **One statement Per line.**
    1. Good
```
if foo == 'blah':
    do_something()
do_one()
do_two()
do_three()
```
    1. Bad
```
if foo == 'blah': do_something()
do_one(); do_two(); do_three()
```


  * Docstrings & Comments
    1. Docstrings = How to use code
    1. Comments = Why (rationale) & how code works