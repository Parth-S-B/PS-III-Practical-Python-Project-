from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age_years = today.year - birth_year
    age_months = today.month - birth_month
    age_days = today.day - birth_day

    if age_days < 0:
        age_months -= 1
        age_days += 30  
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

while True:
    try:
        print("\n--- Age Calculator ---")
        birth_year = int(input("Enter birth year (YYYY): "))
        birth_month = int(input("Enter birth month (1-12): "))
        birth_day = int(input("Enter birth day (1-31): "))

        if not (1 <= birth_month <= 12 and 1 <= birth_day <= 31):
            print("Invalid month or day! Try again.")
            continue

        age_years, age_months, age_days = calculate_age(birth_year, birth_month, birth_day)
        print(f"\nYour Age: {age_years} years, {age_months} months, and {age_days} days.")

        again = input("\nDo you want to calculate another age? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input! Please enter numeric values for year, month, and day.")
