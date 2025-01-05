# Create a function to calculate finances
def calculate_finances(monthly_income: float, tax_rate: float, expenses: float, currency: str) -> None:
    # Do the math for each field
    monthly_tax: float = monthly_income * tax_rate
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


# Create a main entry point for the program
def main() -> None:
    while True:
        try:
            monthly_income: float = float(input('Enter your monthly income: '))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for monthly income.")

    while True:
        try:
            tax_rate: float = float(input('Enter your tax rate (%): '))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for tax rate.")

    while True:
        try:
            expenses: float = float(input('Enter your monthly expenses: '))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for expenses.")

    # Call the function
    calculate_finances(monthly_income, tax_rate, expenses, currency='₹')

# Run the script
if __name__ == "__main__":
    main()


