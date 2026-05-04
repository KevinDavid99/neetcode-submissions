class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for num in tokens:
            if num not in "+-*/":
                stack.append(int(num))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if num == "+":
                    stack.append(num2 + num1)
                if num == "-":
                    stack.append(num2 - num1)
                if num == "*":
                    stack.append(num2 * num1)
                if num == "/":
                    stack.append(int(num2 / num1))
        return stack[-1]


