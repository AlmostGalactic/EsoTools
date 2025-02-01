class Value:
    def __init__(self, value):
        self.value = value

    def set_value(self, new_value):
        self.value = new_value

    def __str__(self):
        return str(self.value)

class Stack:
    def __init__(self):
        self.stack = Value([])
        self.stored_value = ""

    def add_to_stack(self, add: Value):
        self.stack.value.append(add.value)

    def remove_first_item(self):
        self.stack.value.pop(0)

    def clear(self):
        self.stack.value = []

    def reverse(self):
        self.stack.value.reverse()

    def get_first(self):
        return self.stack.value[0]

    def combine_stack(self):
        combined = "".join(map(str, self.stack.value[::-1]))
        self.stack.value.clear()
        self.stack.value = [combined]

    def pop(self, indx = 0):
        popped = self.stack.value.pop(indx)
        return popped

    def pop_stored_value(self):
        popped = self.pop()
        self.stored_value = popped

class Utils:
    def __init__(self):
        pass

    def letter_in_string_is(self, string: Value, indx, equal):
        if 0 <= indx < len(string.value):
            return string.value[indx] == equal
        return False

    def split_by(self, string: Value, by):
        return string.value.split(by)

class VariableManagement:
    def __init__(self, stack: Stack = None, stored_var_name = ""):
        self.variables = {}
        self.stack = stack
        self.stored_var_name = stored_var_name

    def add_modify_variable(self, variable_name, variable_value):
        self.variables[variable_name] = variable_value

    def eval(self, text):
        if self.stack != None:
            self.add_modify_variable(self.stored_var_name, self.stack.stored_value)
        if text in self.variables:
            return self.variables[text]
        return text

class EsolangLexer:
    def __init__(self, text, start_quote, end_quote):
        self.text = text
        self.tokens = []
        self.start_quote = start_quote
        self.end_quote = end_quote

    def split_by(self, by, quotes=True):
        # Removing newlines
        self.text = self.text.replace('\n', ' ').replace('\r', ' ')
        if by != "":
            split = self.text.split(by)
            split = [item for sublist in zip(split, [' '] * len(split)) for item in sublist][:-1]
        else:
            split = list(self.text)  # Splitting by every character without extra spaces
        self.tokens = split
        if quotes:
            self.combine_quoted_segments()
        self.remove_all_occurrences(" ")
        self.remove_all_occurrences("   ")

        return self

    def remove_all_occurrences(self, item_to_remove):
        while item_to_remove in self.tokens:
            self.tokens.remove(item_to_remove)

    def combine_quoted_segments(self):
        combined_list = []
        inside_quotes = False
        temp_str = ""

        for item in self.tokens:
            if self.start_quote in item and self.end_quote in item:
                # Handle case where both start and end quotes are in the same token
                temp_str = item.replace(self.start_quote, "").replace(self.end_quote, "").strip()
                combined_list.append(temp_str)
                temp_str = ""
            elif self.start_quote in item:
                inside_quotes = True
                temp_str += item.replace(self.start_quote, "")
            elif self.end_quote in item and inside_quotes:
                inside_quotes = False
                temp_str += item.replace(self.end_quote, "")
                combined_list.append(temp_str.strip())
                temp_str = ""
            elif inside_quotes:
                temp_str += item
            else:
                combined_list.append(item)

        if temp_str:
            combined_list.append(temp_str)  # Handle any remaining unclosed quote segment

        self.tokens = combined_list
