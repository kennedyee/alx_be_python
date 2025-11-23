# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'
    
    Returns:
        float or str: Result of the operation or error message
    """

    match operation:
        case "add":
            return num1 + num2
        
        case "subtract":
            return num1 - num2
        
        case "multiply":
            return num1 * num2
        
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        
        case _:
            return "Error: Invalid operation"
