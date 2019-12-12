
#gathering user inputs, turning it into a useable number
user_input = input("How much money do you have? ")
user_input = float(user_input) * 100
user_input = int(user_input)
#divide user inputs into different types of change
quarters = user_input // 25
remainder = user_input % 25
dimes = remainder // 10
remainder = remainder % 10
nickles = remainder // 5
remainder = remainder % 5
penny = remainder // 1
#telling them how much change they have
print(f"You have {quarters} quarter(s), {dimes} dime(s), {nickles} nickle(s), and {penny} pennie(s)")
