import math
from fpdf import FPDF

def calculate_total():
    print("Welcome to our receipt calculator.")
    
    # Step 1: Get all the items, their prices, and quantities
    items = []
    while True:
        name = input("Enter the item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input(f"Enter the price of {name}: "))
        quantity = int(input(f"Enter the quantity of {name}: "))
        items.append((name, price, quantity))

    # Step 2: Calculate subtotal
    subtotal = sum(price * quantity for name, price, quantity in items)
    print(f"Subtotal: ${round(subtotal, 2)}")
    
    # Step 3: Get sales tax and tip percentages
    tax_p = float(input("What is the sales tax in your area (in %)? "))
    tip_p = float(input("What percentage would you like to give as a tip? (in %) "))

    # Step 4: Calculate tax and tip amounts
    tax_amount = subtotal * (tax_p / 100.0)
    tip_amount = subtotal * (tip_p / 100.0)

    # Step 5: Get any discount information (optional)
    discount_p = float(input("Any discount applied? (in % or enter 0 for no discount) "))
    discount_amount = subtotal * (discount_p / 100.0)

    # Step 6: Final total calculation
    total = subtotal + tax_amount + tip_amount - discount_amount
    print(f"Total (after tax, tip, and discount): ${round(total, 2)}")

    # Step 7: Get how many people to split the bill with
    split = int(input("How many people are splitting the bill? "))
    cost_per_person = total / split
    print(f"The total cost per person is: ${round(cost_per_person, 2)}")

    # Generate receipt
    receipt = generate_receipt(items, subtotal, tax_amount, tip_amount, discount_amount, total, split)

    # Step 8: Save receipt to file
    save_option = input("Would you like to save the receipt as a text file or PDF? (text/pdf): ")
    file_name = input("Enter the file name (without extension): ")
    if save_option.lower() == 'text':
        save_as_text(receipt, file_name)
    elif save_option.lower() == 'pdf':
        save_as_pdf(receipt, file_name)

def generate_receipt(items, subtotal, tax_amount, tip_amount, discount_amount, total, split):
    # Create and return the receipt as a string
    receipt = "\n==== Receipt ====\n"
    for name, price, quantity in items:
        receipt += f"{name}: ${price} x {quantity} = ${round(price * quantity, 2)}\n"
    
    receipt += f"\nSubtotal: ${round(subtotal, 2)}"
    receipt += f"\nTax: ${round(tax_amount, 2)}"
    receipt += f"\nTip: ${round(tip_amount, 2)}"
    receipt += f"\nDiscount: -${round(discount_amount, 2)}"
    receipt += f"\nTotal: ${round(total, 2)}"
    receipt += f"\nSplit between {split} people: ${round(total/split, 2)} per person"
    receipt += "\n===================="
    
    # Print receipt
    print(receipt)
    
    return receipt

def save_as_text(receipt, file_name):
    # Save the receipt as a text file
    with open(f"{file_name}.txt", 'w') as file:
        file.write(receipt)
    print(f"Receipt saved as {file_name}.txt")

def save_as_pdf(receipt, file_name):
    # Save the receipt as a PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Split the receipt text into lines and add them to the PDF
    for line in receipt.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

    # Save the PDF to the specified file
    pdf.output(f"{file_name}.pdf")
    print(f"Receipt saved as {file_name}.pdf")

# Run the calculator
calculate_total()
