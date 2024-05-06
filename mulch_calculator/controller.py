


# Functions
def calculate_mulch(a: int, d: int) -> int:
    mulch = (a*100)*(d*0.1)
    return mulch

def display_results(m: int) -> str:
    output = f"The amount of mulch needed is {m} liters/cubic decimeters."
    return output

# Global Scope
if __name__ == "__main__":
    print("Global scope")