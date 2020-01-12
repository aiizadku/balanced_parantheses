# Write a FUNCTION called BALANCE which takes an INPUT STRING
# Create an OUTPUT variable and set it equal to []
# Create an OPENED_INDEXES variable and set it equal to []
# Iterate over the INPUT STRING, save each character as CHARACTER
#   - If CHRACTER is NOT '(' or ')', add onto OUTPUT
#   - If CHARACTER is '('
#     - Get the length of OUTPUT and add it to OPENED_INDEXES because you will want to add the '(' character to OUTPUT at that index
#   - If CHRACTER is ')'
#     - See if OPENED_INDEXES has a length greater than 0
#       - If true
#         - Pop off the last item of OPENED_INDEXES, save as LAST_OUTPUT_INDEX
#         - Add '(' where LAST_OUTPUT_INDEX to OUTPUT
#         - Add the ')' to OUTPUT
#       - If false
#         - Do nothing because the the ')' character you're talking about is not legit
# Return OUTPUT as a joined string

def balance(input_string):
    output = []
    opened_indexes = []
    for character in input_string:
        if character == '(':
            opened_indexes.append(len(output))
        elif character == ')':
          if len(opened_indexes) > 0:
              last_output_index = opened_indexes.pop()
              output.insert(last_output_index, '(')
              output.append(character)
        else:
            output.append(character)
    return ''.join(output)

print(balance("()") == "()")
print(balance("a(b)c)") == "a(b)c")
print(balance("(a)(bdd)c)") == "(a)(bdd)c")
print(balance("a(dbvb)c)") == "a(dbvb)c")
print(balance("a(b)(c)())") == "a(b)(c)()")
print(balance(")(") == "")
print(balance("(((((") == "")
print(balance(")(())(") == "(())")
print(balance("(()()(") == "()()")
print(balance(")())(()()(") == "()()()")