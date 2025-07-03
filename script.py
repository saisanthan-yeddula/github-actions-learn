def greet_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    try:
        age = int(age)
    except ValueError:
        print("❌ Age must be a number.")
        return

    print(f"👋 Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    greet_user()
