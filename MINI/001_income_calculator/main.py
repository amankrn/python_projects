# Create a function to calculate finances
def calculate_finances(monthly_income: float, tax_rate: float, expenses: float, currency: str) -> None:
    # Do the math for each field
    monthly_tax: float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax
    monthly_leftover: float = monthly_net_income - expenses
    yearly_income: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_income - yearly_tax
    yearly_expenses: float = expenses * 12
    yearly_leftover: float = yearly_net_income - yearly_expenses

    # Format the information nicely for the user
    print('--------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Monthly expenses: {currency}{expenses:,.2f}')
    print(f'Monthly leftover: {currency}{monthly_leftover:,.2f}')
    print(f'Yearly salary: {currency}{yearly_income:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print(f'Yearly expenses: {currency}{yearly_expenses:,.2f}')
    print(f'Yearly leftover: {currency}{yearly_leftover:,.2f}')
    print('--------------------------------')

# get_positive_input function
def get_positive_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Create a main entry point for the program
def main() -> None:
    # Get user input
    currency: str = '₹'
    monthly_income: float = get_positive_input(f"Enter your monthly income(in {currency}) : ")
    tax_rate: float = get_positive_input("Enter your tax rate as a percentage (e.g., 20 for 20%): ")
    expenses: float = get_positive_input(f"Enter your monthly expenses(in {currency}) : ")

    # Call the function
    calculate_finances(monthly_income, tax_rate, expenses, currency)

# Run the script
if __name__ == "__main__":
    main()


