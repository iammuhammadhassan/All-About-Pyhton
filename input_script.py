# Example: Using Python's input() function
# This script demonstrates how to use input() properly
# Run this from terminal: python input_script.py

print("=" * 50)
print("Python input() Function Examples")
print("=" * 50)

# Example 1: Simple text input
name = input("What is your name? ")
print(f"Hello, {name}!")

# Example 2: Number input
age = int(input("How old are you? "))
print(f"Next year you will be {age + 1} years old")

# Example 3: Multiple inputs
print("\n--- Get user details ---")
email = input("Enter your email: ")
country = input("Enter your country: ")
print(f"\nYour email: {email}")
print(f"Your country: {country}")

# Example 4: Getting choice
print("\n--- Make a choice ---")
choice = input("Enter 'a', 'b', or 'c': ").lower()
if choice == 'a':
    print("You chose A")
elif choice == 'b':
    print("You chose B")
elif choice == 'c':
    print("You chose C")
else:
    print("Invalid choice!")

print("\n" + "=" * 50)
print("Done!")
print("=" * 50)
