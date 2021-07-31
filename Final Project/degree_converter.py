# Develop a python based degree converter which takes °C value and give you output of °F.
# Formula for Conversion: ___°C × 9/5) + 32 = ___°F
 
celsius = int(input("enter the temperature in celsius: "))    #user enter temperature in celsius 
Fahrenheit = (celsius * 9 / 5)  + 32                 # convert  celsius to fahrenheit
print('%.1f°C is equivalent to %.1f°F'%(celsius, Fahrenheit))   # print the converted temperature

# Input - 1:
#enter the temperature in celsius: 50

# Output - 1:
# 50.0°C is equivalent to 122.0°F

# Input - 2:
#enter the temperature in celsius: 37

# Output - 2: 
# 37.0°C is equivalent to 98.6°F
