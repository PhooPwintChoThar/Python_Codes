def count_operands(expression):
    if isinstance(expression, int):
        return 1
    
    return count_operands(expression[0])+count_operands(expression[2])


print(count_operands(((((2,'+',4),'/',3),'*',2),'+',(3, '**', 4))))
