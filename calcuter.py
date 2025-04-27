def calculator():
    print("Welcome to the Real-Feel Calculator!")
    print("-------------------------------------")
    last_answer = 0
    
    while True:
        print("\nOptions:")
        print(" Type your expression (e.g., 4+5*6-3)")
        print(" Type 'ans' to use the last answer")
        print(" Type 'clear' to reset last answer to 0")
        print(" Type 'exit' to quit")
        
        expression = input("\nEnter your calculation: ")
        
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        elif expression.lower() == 'clear':
            last_answer = 0
            print("Memory cleared. Last answer reset to 0.")
            continue
        elif 'ans' in expression:
            expression = expression.replace('ans', str(last_answer))
        
        try:
            # Safely evaluate the expression
            result = eval(expression)
            print(f"Result: {result}")
            last_answer = result
        except Exception as e:
            print(f"Error: {e}")

calculator()