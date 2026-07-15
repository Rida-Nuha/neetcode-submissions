class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for chars in tokens:
            if chars not in ("+", "-", "*","/"):
                stack.append(int(chars))

            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if chars == "+":
                    stack.append(num1 + num2)
                elif chars == "-":
                    stack.append(num2 - num1)
                elif chars == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num2 / num1))

        return stack.pop()
                      