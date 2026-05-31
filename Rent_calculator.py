# Work Flow
# 1. Get the total rent amount from the user
# 2. Get the number of people sharing the rent from the user
# 3. Calculate the amount each person has to pay by dividing the total rent by the number of people
# 4. Display the amount each person has to pay
# Get the total rent amount from the user
total_rent = float(input("Enter the total rent amount: "))
# Get the number of people sharing the rent from the user
num_people = int(input("Enter the number of people sharing the rent: "))
# Calculate the amount each person has to pay
amount_per_person = total_rent / num_people
# Display the amount each person has to pay
print(f"Each person has to pay: {amount_per_person:.2f}")
