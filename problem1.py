# Problem 1
# Sang Park

while True:
    try:
        fahrenheit = input("Enter a temperature in Fahrenheit: ")
        
        fahrenheit = float(fahrenheit)
        
        celsius = 5/9 * (fahrenheit - 32)

        print(f"Temperature in Celsius: {round(celsius, 2)}°C")   
            
        break     
        
    except ValueError:
        print("Invalid input. Please enter a valid numerical temperature.")
        
   
