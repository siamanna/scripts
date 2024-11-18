from datetime import datetime

def calculate_difference(start_date, end_date):
    delta = end_date - start_date if end_date >= start_date else start_date - end_date

    years = delta.days // 365
    remaining_days = delta.days % 365
    months = remaining_days // 30  
    remaining_days %= 30

    weeks = remaining_days // 7
    days = remaining_days % 7

    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    return years, months, weeks, days, hours, minutes, seconds

def main():
    print("Choose an option:")
    print("1. From now to a future date")
    print("2. From now to a past date")
    print("3. Between two custom dates")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        target_date_str = input("Enter the target date (YYYY-MM-DD): ")
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        years, months, weeks, days, hours, minutes, seconds = calculate_difference(current_date, target_date)
        print(f"Time until {target_date}: {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    
    elif choice == 2:
        target_date_str = input("Enter the past date (YYYY-MM-DD): ")
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        years, months, weeks, days, hours, minutes, seconds = calculate_difference(target_date, current_date)
        print(f"Time since {target_date}: {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    
    elif choice == 3:
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        years, months, weeks, days, hours, minutes, seconds = calculate_difference(start_date, end_date)
        if end_date >= start_date:
            print(f"Time between {start_date} and {end_date}: {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
        else:
            print(f"Time between {end_date} and {start_date}: {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
