def calculate_bmi(weight, height):
    # Formula for BMI: weight (kg) / (height (m) ** 2)
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    bmi_category = interpret_bmi(bmi)

    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {bmi_category}")

if __name__ == "__main__":
    main()
