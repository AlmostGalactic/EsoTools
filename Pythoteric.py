from EsolangTool.EsolangTool import *

def RunCode(code, debug = False):
    stack = Stack()
    tokens = EsolangLexer(code, "[", "]").split_by(" ").tokens
    variables = VariableManagement(stack, "STORED_VAR")

    index = 0
    while index < len(tokens):
        command = tokens[index]
        if command == "PRINT":
            index += 1
            print(variables.eval(tokens[index]))
        elif command == "VAR":
            index += 1
            var_name = tokens[index]
            index += 1
            var_val = tokens[index]
            variables.add_modify_variable(var_name, variables.eval(var_val))
        elif command == "ADD":
            index += 1
            stack.add_to_stack(Value(tokens[index]))
        elif command == "POP":
            stack.pop_stored_value()
        elif command == "IGNORE":
            index += 1
        elif command == "CLEAR":
            stack.clear()
        elif command == "ADDITION":
            left = int(variables.eval(stack.pop()))
            right = int(variables.eval(stack.pop()))
            stack.add_to_stack(Value(left+right))
        elif command == "SUBTRACTION":
            left = int(variables.eval(stack.pop()))
            right = int(variables.eval(stack.pop()))
            stack.add_to_stack(Value(left-right))
        elif command == "DIVISIOM":
            left = int(variables.eval(stack.pop()))
            right = int(variables.eval(stack.pop()))
            stack.add_to_stack(Value(left/right))
        elif command == "MULTIPLICATION":
            left = int(variables.eval(stack.pop()))
            right = int(variables.eval(stack.pop()))
            stack.add_to_stack(Value(left*right))
        elif command == "MODULUS":
            left = int(variables.eval(stack.pop()))
            right = int(variables.eval(stack.pop()))
            stack.add_to_stack(Value(left%right))
        elif command == "PROMPT":
            stack.add_to_stack(Value(str(input("? "))))

        index += 1
    if debug:
        print(tokens)
        print(stack.stack)
        print(stack.stored_value)
        print(variables.variables)

code ="""
PROMPT
PROMPT
SUBTRACTION
POP
PRINT STORED_VAR
"""
RunCode(code)