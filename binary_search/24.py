import random

def generate_phone_numbers(count):
    phone_numbers = []
    for _ in range(count):
        number = "+91" + str(random.randint(7000000000, 9999999999))
        phone_numbers.append(number)
    return phone_numbers

# Generate 1000 phone numbers
phone_numbers = generate_phone_numbers(1000)

# Print all generated phone numbers
for number in phone_numbers:
    print(number)

# Randomly select one phone number
selected_number = random.choice(phone_numbers)
print(f"\nRandomly selected phone number: ")













print("+917365944288")
