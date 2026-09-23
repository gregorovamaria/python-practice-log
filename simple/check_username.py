"""
Checks username's validity based on these rules:
1. Username length must be between 5 and 15 characters
2. It must contain only alphanumeric characters
3. It must start with letter
"""

def check_username(name: str) -> str:
    """Checks username's validity based on length, charset, and starting char."""
    errors = []

    if not (5 <= len(name) <= 15):
        errors.append("must be between 5 and 15 characters long")

    if not name.isalnum():
        errors.append("only letters and numbers are allowed")

    if not (name and name[0].isalpha()):
        errors.append("must start with letter")

    if not errors:
        return "Valid username"

    if len(errors) == 1:
        details = errors[0]
    elif len(errors) == 2:
        details = f'{errors[0]}, and {errors[1]}'
    else:
        details = f"{', '.join(errors[:-1])}, and {errors[-1]}"

    return f"Invalid username: {details}"

    
def main() -> None:
    test_cases = ["#@$", "", "user1", "123user", "validUser99", "a" * 20]
    for username in test_cases:
        print(f'{repr(username):<15} -> {check_username(username)}')

if __name__ == "__main__":
    main()
