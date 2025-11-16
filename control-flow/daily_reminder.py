# Personal Daily Reminder Program

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority levels using match case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Time sensitivity check
if time_bound == "yes":
    # Immediate action required
    print(f"\nReminder: {base_message} that requires immediate attention today!")
else:
    # No immediate action required
    print(f"\nNote: {base_message}. Consider completing it when you have free time.")
