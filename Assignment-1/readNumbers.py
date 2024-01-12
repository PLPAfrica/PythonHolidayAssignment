def read_numbers():
    try:
        # Reading a list of numbers from the user
        numbers = list(map(float, input("Enter a list of numbers separated by space: ").split()))
        return numbers
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return []

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

def find_maximum(numbers):
    return max(numbers) if len(numbers) > 0 else None

def find_minimum(numbers):
    return min(numbers) if len(numbers) > 0 else None

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def main():
    numbers = read_numbers()

    if numbers:
        print("Sum:", calculate_sum(numbers))
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_maximum(numbers))
        print("Minimum:", find_minimum(numbers))
        print("Filtered Odd Numbers:", filter_even_numbers(numbers))

if __name__ == "__main__":
    main()
