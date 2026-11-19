
# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

valid = False

# ---------- PART 1: retry loop ----------
while not valid:

    # ---------- PART 2: input and calculation ----------
    try:
        bill = float(input("Enter the total bill: "))
        discount = float(input("Enter discount percentage: "))
        people = int(input("Enter number of people: "))

        # Calculate discount
        discount_amount = bill * discount / 100

        # Calculate final bill
        final_bill = bill - discount_amount

        # Calculate amount per person
        amount_per_person = final_bill / people

    # ---------- PART 3: handle errors ----------
    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("Number of people cannot be 0.")

    # ---------- PART 4: else and finally ----------
    else:
        print("Final bill:", final_bill)
        print("Each person pays:", amount_per_person)

        valid = True

    finally:
        print("Attempt finished.")
