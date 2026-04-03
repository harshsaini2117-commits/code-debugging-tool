def check_syntax(code):
    errors = []
    try:
        compile(code, '<string>', 'exec')
    except SyntaxError as e:
        errors.append(f"Syntax Error: {e}")
    return errors


def check_logic(code):
    issues = []

    if "==" in code and "if" not in code:
        issues.append("Possible logic issue: '==' used without condition")

    if "(" in code and ")" not in code:
        issues.append("Missing closing parenthesis")

    return issues


def analyze_code(code):
    syntax_errors = check_syntax(code)
    logic_issues = check_logic(code)

    return {
        "syntax_errors": syntax_errors,
        "logic_issues": logic_issues
    }


code_input = input("Enter your code:\n")
result = analyze_code(code_input)

print("\nAnalysis Result:")
print(result)
