def greet(name):
    """
    A simple function to greet a user by name.

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the Python world."

# Example usage:
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
