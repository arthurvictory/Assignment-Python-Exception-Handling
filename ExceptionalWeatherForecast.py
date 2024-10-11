# Objective: The aim of this assignment is to enhance your understanding of exception 
# handling by creating a weather forecast application that gracefully handles unexpected 
# user input and provides user-friendly error messages.

# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature 
# to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process. What happens 
# if they type out "thirty" instead of doing 30?

# Task 3: User Experience Implement an else block that prints the converted temperature 
# in a user-friendly format. 

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally Add a finally block that thanks the user for using the weather forecast 
# application, ensuring that this message is displayed regardless of whether an exception 
# was caught or not.

# Function that inputs Fahrenheit temp
def get_temp():
    while True:
        try:
            return float(input("Enter your temperature in Fahrenheit: "))
        except ValueError:
            print(f"You did not enter a proper integer for the temp! Try Again.")


# SImple function to convert Fahrenheit into Celsius
def convert_to_celsius(Fahrenheit):
            return (Fahrenheit - 32) * 5/9

# Function that tells the weather forecast based on temperatures
def weather_forecast():
    fahrenheit_temp = get_temp()
    try:
        celsius_temp = convert_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp} degrees Fahrenheit is {celsius_temp} degrees Celsius")
    except Exception as e:
         print(f"An error occurred: {e}")
    finally:
         print("Thank you for using the weather forecast app for all your needs!")

weather_forecast()