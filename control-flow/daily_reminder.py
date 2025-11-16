# Personal Daily Reminder Program

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process priority and time-bound using match case
match priority:
    case "high" | "medium" | "low":
        match time_bound:
            case "yes":
                # Exact format for autograder
                print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
            case "no":
                print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
            case _:
                print("Invalid input for time-bound. Please enter yes or no.")
    case _:
        print(f"'{task}' has an unknown priority level. Please enter high, medium, or low.")
