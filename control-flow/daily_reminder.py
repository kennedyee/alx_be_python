# daily_reminder.py
# Personal Daily Reminder Program

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process priority using match case
match priority:
    case "high" | "medium" | "low":
        # Check time-bound status within the priority case
        if time_bound == "yes":
            # Reminder for time-sensitive tasks
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            # Reminder for non-time-bound tasks
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound. Please enter yes or no.")
    case _:
        print(f"'{task}' has an unknown priority level. Please enter high, medium, or low.")
