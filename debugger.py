def check_code(code):
    errors = []

    if "==" in code and "if" not in code:
        errors.append("Possible logical error: '==' used without condition")

    if "(" in code and ")" not in code:
        errors.append("Syntax Error: Missing closing parenthesis")

    if ":" in code and "if" not in code and "for" not in code:
        errors.append("Syntax Error: ':' used incorrectly")

    if len(errors) == 0:
        return "No obvious errors found"
    
    return errors


code_input = input("Enter your code: ")
result = check_code(code_input)

print("Result:")
print(result)