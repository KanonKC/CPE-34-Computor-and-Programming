class py_solution:
    def __init__(self,text):
        self.text = text

    def is_valid_parentheses(self):
        openParent = ['(','[','{']
        closeParent= [')',']','}']
        stack = []
        for i in range(len(self.text)):
            if self.text[i] in openParent: # Start Always Start as OPEN
                stack.append(self.text[i])
            elif self.text[i] in closeParent: #
                if len(stack) == 0:
                    return False
                if closeParent.index(self.text[i]) == openParent.index(stack[-1]):
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

x = py_solution(input("input: "))
if x.is_valid_parentheses():
    print('valid parentheses')
else:
    print('invalid parentheses')