#  BMI Calculator Function

#    * Create a reusable function with parameters for height and weight.
#    * Display BMI value and category.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi, category = calculate_bmi(weight, height)

print(f"\nBMI: {bmi:.2f}")
print("Category:", category)