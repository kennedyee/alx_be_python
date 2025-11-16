# Daily Reminder Program

# Asking for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority description
match priority:
    case "high":
        priority_text = "a high priority task"
    case "medium":
        priority_text = "a medium priority task"
    case "low":
        priority_text = "a low priority task"
    case _:
        priority_text = "a task with unknown priority"

# Time-bound condition
if time_bound == "yes":
    # This is the required EXACT PHRASE from the task
    print(f"\nReminder: '{task}' is {priority_text} that requires immediate attention today!")
else:
    # For non-time-bound tasks
    print(f"\nNote: '{task}' is {priority_text}. Consider completing it when you have free time.")
