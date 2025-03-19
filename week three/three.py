def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")