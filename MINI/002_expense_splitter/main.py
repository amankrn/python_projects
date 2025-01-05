# Description: A simple script to split expenses among a group of people.
def calculate_split(total_amount: float, splits: list[float], currency: str) -> None:
    # Validate the splits
    if sum(splits) != 100:
        raise ValueError('The splits must add up to 100%.')
    # Perform the calculation
    shares = [total_amount * (split / 100) for split in splits]

    # Format the results and display them
    print(f'Total expense: {currency}{total_amount:,.2f}')
    for i, share in enumerate(shares, 1):
        print(f'Person {i} should pay: {currency} {share:,.2f}')

# Create a function to get the total amount
def get_total_amount() -> float:
    while True:
        try:
            return float(input('Enter total amount: '))
        except ValueError:
            print('Invalid input. Enter a numeric value.')

# Create a function to get the number of people
def get_number_of_people() -> int:
    while True:
        try:
            no_people:int = int(input('Enter number of people: '))
            if no_people <= 0:
                print('Number of people should be greater than 0.')
            else:
                return no_people
        except ValueError:
            print('Invalid input. Enter an integer.')

# Create a function to get the percentage input
def get_percentage_input(person_num: int, remaining: float) -> float:
    while True:
        try:
            split = float(input(f'Enter the percentage for person {person_num}: '))
            if split > remaining:
                print(f'Invalid input. Enter a percentage less than or equal to {remaining:.2f}.')
            else:
                return split
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

# Create a main entry point
def main() -> None:
    # 6. Try to get the user input and perform the calculation
    total_amount: float = get_total_amount()
    number_of_people: int = get_number_of_people()  
    
    while True:
        try:
            split_srt: str = input('Do you want to split the expense equally among all people? (y/n): ')
            if split_srt not in ['y', 'Y', 'n', 'N', 'yes', 'YES', 'no', 'NO']:
                raise ValueError
            equal_split: bool = split_srt in ['y', 'Y', 'yes', 'YES']
            break
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    if equal_split:
        splits = [100 / number_of_people] * number_of_people
    else:
        splits = []
        remaining_sharing: float = 100
        for i in range(number_of_people):
            if remaining_sharing == 0:
                print('The remaining percentage is 0. No further input needed.\n Rest people will not be sharing the expense.')
                splits.extend([0] * (number_of_people - i))
                break
            elif i == number_of_people - 1:
                print(f"Person {i + 1} will be sharing the remaining {remaining_sharing:.2f}%.")
                split = remaining_sharing
            else:
                print(f"To split the remaining {remaining_sharing:.2f}% among the remaining {number_of_people - i} people.")
                split = get_percentage_input(i + 1, remaining_sharing)
                remaining_sharing -= split
            splits.append(split)

    # Call the function to calculate and display expenses
    calculate_split(total_amount, splits, currency='€')

# Run the script
if __name__ == '__main__':
    main()