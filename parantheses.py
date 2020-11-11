def balance(string):
    right_stack = []
    left_stack = []
    for i, element in enumerate(string):
        if element == "(":
            left_stack.append(i)
        elif element == ")":
            if left_stack:
                left_stack.pop()
            else:
                right_stack.append(i)
    combined_arr = right_stack + left_stack
    final_string = ""
    for i,element in enumerate(string):
        if i not in combined_arr:
            final_string += string[i]

    return final_string

    


print (balance("()")) # should return "()"
print (balance("a(b)c)")) # should return "a(b)c"
print (balance("(a)(bdd)c)")) # should return "(a)(bdd)c"
print (balance("a(dbvb)c)")) # should return "a(dbvb)c"
print (balance("a(b)(c)())")) # should return "a(b)(c)()"
print (balance(")(")) # should return ""
print (balance("(((((")) # should return ""
print (balance(")(())(")) # should return "(())"
print (balance("(()()(")) # should return "()()"
print (balance(")())(()()(")) # should return "()()()" 

