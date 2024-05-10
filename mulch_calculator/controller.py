"""
controller.py
by Filip Novotny
Adds functionality to the program:
* gets values as integers
* uses these values in the formula used for calculation
* returns and displays the result as a string
"""

# Define functions
# Calculate equation
def calculate_mulch(a: int, d: int) -> int:
    mulch = (a*100)*(d*0.1)
    return round(mulch, 2)

# Return and display
def display_results(m: int) -> str:
    output = f"The amount of mulch needed is {m} liters/cubic decimeters."
    return output

# Global Scope
if __name__ == "__main__":
    print("Global scope")