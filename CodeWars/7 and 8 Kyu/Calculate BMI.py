def bmi(weight, height):
    thebmi = weight/(height*height)
    if thebmi <= 18.5:
        return "Underweight"
    elif thebmi <= 25:
        return "Normal"
    elif thebmi <= 30:
        return "Overweight"
    else:
        return "Obese"