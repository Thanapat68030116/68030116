def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def sine_taylor(x, terms=10):
    sine = 0
    for n in range(terms):
        sign = (-1) ** n
        term = (x ** (2*n + 1)) / factorial(2*n + 1)
        sine += sign * term
    return sine

def degrees_to_radians(deg):
    return deg * (3.141592653589793 / 180)

angle_deg = float(input("ป้อนมุม (องศา): "))
x = degrees_to_radians(angle_deg)

sine_value = sine_taylor(x)
print(f"Sine({angle_deg}°) ≈ {sine_value}")