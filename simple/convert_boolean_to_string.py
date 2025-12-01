"""Convert boolean value to string and print the value to terminal."""


def boolean_to_string(b: bool) -> str:
    """Return string converted from boolean."""
    # if b is True:
    #     return "True"

    # return "False"

    if type(b) != bool:
        raise ValueError("Input must be boolean.")

    return str(b)


def main() -> None:
    """Print boolean value converted to string to terminal as well as the type of the value."""
    value = boolean_to_string("False")
    print(f"value: {value}")
    print(f"type of the value: {type(value)}")


if __name__ == "__main__":
    main()
