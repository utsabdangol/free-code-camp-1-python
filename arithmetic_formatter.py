def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check if the operator is valid
        if operator not in {"+", "-"}:
            return "Error: Operator must be '+' or '-'."

        # Check if both numbers contain only digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Convert numbers to integers
        num1, num2 = int(num1), int(num2)

        # Check if numbers are too large (limit to 4 digits)
        if num1 > 9999 or num2 > 9999:
            return "Error: Numbers cannot be more than four digits."

        # Determine width for formatting (based on longest number + operator space)
        width = max(len(str(num1)), len(str(num2))) + 2

        # Format each line
        first_line.append(str(num1).rjust(width))
        second_line.append(operator + " " + str(num2).rjust(width - 2))
        dashes.append("-" * width)

        # Compute result if show_answers is True
        if show_answers:
            result = num1 + num2 if operator == "+" else num1 - num2
            results.append(str(result).rjust(width))

    # Join all parts with spacing of 4 spaces between problems
    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dashes)
    ])
    
    # Add results if show_answers is True
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems


# Test the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
