    def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def fahrenheit_para_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

print(temp_celsius, "graus Celsius equivalem a", celsius_para_fahrenheit(temp_celsius), "graus Fahrenheit.")
print(temp_fahrenheit, "graus Fahrenheit equivalem a", fahrenheit_para_celsius(temp_fahrenheit), "graus Celsius.")