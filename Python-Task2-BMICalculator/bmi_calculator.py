print("====== BMI Calculator ======")

while True:
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive values.")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("\n----- BMI Result -----")
        print("BMI:", round(bmi, 2))
        print("Category:", category)

        break

    except ValueError:
        print("Error: Please enter numeric values only.")