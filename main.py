def bracketcheck(text):
    openbrackets = ['(', '[', '{']
    closebrackets = [')', ']', '}']
    stack = []
    for i in text:
        if i in closebrackets:
            if stack[-1] == openbrackets[closebrackets.index(i)] and stack:  # popping from stack if closing last bracket
                stack.pop()
                continue
            else:
                return False
        elif i in openbrackets:
            stack.append(i)
    if not stack:
        return True
    else:
        return False

text= "{[()]"
print(bracketcheck(text))
