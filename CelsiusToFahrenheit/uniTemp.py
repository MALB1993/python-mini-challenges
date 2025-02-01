def main():
    temp = float(input("What's your temp : "))
    unit = input("c or f ? (c = Celsius / f = fahrenheit ) : ")
    print(convert_temp(temp, unit))

def convert_temp(temp, unit):
    unit = unit.lower()
    
    if unit == "c":
        return f"{temp} C° = {(temp * 1.8) + 32} F°"
    elif unit == "f":
        return f"{temp} F° = {(temp - 32) * 5/9:.2f} C°"  
    else:
        return "Invalid unit!"

main()