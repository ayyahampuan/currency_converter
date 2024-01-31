class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("Invalid currencies. Please enter valid currency codes.")
            return None

        exchange_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        converted_amount = amount * exchange_rate

        return converted_amount

def main():
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'INR': 73.91,  # Example: 1 USD = 73.91 INR
    }

    converter = CurrencyConverter(exchange_rates)

    print("Welcome to the Currency Converter!")

    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            from_currency = input("Enter the currency code to convert from (e.g., USD): ").upper()
            to_currency = input("Enter the currency code to convert to (e.g., EUR): ").upper()

            if from_currency == to_currency:
                print("Please enter different currencies for conversion.")
                continue

            amount = float(input("Enter the amount to convert: "))

            converted_amount = converter.convert(amount, from_currency, to_currency)

            if converted_amount is not None:
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        elif choice == '2':
            print("Exiting the Currency Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-2).")

if __name__ == "__main__":
    main()
