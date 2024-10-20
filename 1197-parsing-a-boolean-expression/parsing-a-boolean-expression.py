class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        bool_map = defaultdict(bool)
        bool_map['t'] = True
        bool_map['f'] = False
        ops = ["&", "!", "|"]
        operation_stack = []
        operand_stack = []
        
      
        for ch in expression:
            if ch in ops:
                operation_stack.append(ch)

            elif ch == ")":
                op = operation_stack[-1]
                res = None
                if op == "&":
                    res = True
                    while operand_stack[-1] != "(":
                        temp = operand_stack.pop()
                        res = res and temp

                elif op == "|":
                    res = False
                    while operand_stack[-1] != "(":
                        temp = operand_stack.pop()
                        res = res or temp
                else:
                    # not
                    while operand_stack[-1] != "(":
                        temp = operand_stack.pop()
                        res = not temp

                operation_stack.pop()
                operand_stack.pop()
                operand_stack.append(res)

            elif ch in bool_map:
                operand_stack.append(bool_map[ch])
            
            elif ch == "(":
                operand_stack.append(ch)
             

        return operand_stack[-1]
