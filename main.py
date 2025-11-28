def generate_dummy_dict(n):
    dummy_dict = {}
    for i in range(1, n + 1):
        key = f"key{i}"
        value = f"value{i}"
        dummy_dict[key] = value
    return dummy_dict


def main():
    try:
        n = int(input("Enter number of keys: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
        
        result = generate_dummy_dict(n)
        print("\nGenerated Dummy Dictionary:")
        print(result)

    except ValueError:
        print("Invalid input! Enter a valid number.")


if __name__ == "__main__":
    main()
