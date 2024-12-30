class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        def calculate(num1, num2, operator):
            match operator:
                case '*':
                    return num1 * num2
                case '-':
                    return num1 - num2
                case '+':
                    return num1 + num2
                case '/':
                    return int(num1 / num2)

        stack = []

        for i in range(len(tokens)):

            if tokens[i] not in {'+', '/', '-', '*'}:
                stack.append(tokens[i])

            else:
                number2 = int(stack.pop())
                number1 = int(stack.pop())
                result = calculate(number1, number2, tokens[i])
                stack.append(result)

        return stack[0] 
