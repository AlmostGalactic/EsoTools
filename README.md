# EsoTools
Just some tools that  might or might not help you with making esolangs

## Contains
- stack
- simple customizable lexer
- Variable Management
- some utilities

## How to use

First you want to import the python library

```py
from EsolangTool import *
```

### Stack
Now the first thing is the stack. The stack is pretty simple, here is how to set it up

```py
stack = Stack()
```
If you want to add something to the stack you need to use the Value() class

here is how
```py
stack.add_to_stack(Value(add))
```
the value is just a value not too complicated


If you want to remove the first item in the stack you can do
```py
stack.remove_first_item()
```
or you can clear stack like this
```py
stack.clear()
```

Here is a list of all the rest of the stack methods
```py
stack.reverse() # reverses the stack
stack.get_first() # returns the first item of the stack
stack.combine_stack() # combines the stack top to bottom
stack.pop(index<-OPTIONAL) # pops the top item in the stack and returns it
stack.pop_stored_value() # pops the top item and stoes it in the stacks "stored_variable" if you need it later
```

### Utils
kinda self explanatory if you look in the class

### 
