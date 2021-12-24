#TempConvert.py

TempStr = input("Please input Tempreture with sign (C/F) : ")

if TempStr[-1] in ['F' , 'f']:
    Centigrade = (eval(TempStr[0:-1]) - 32)/1.8
    print("{:.2f}C".format(Centigrade))
elif TempStr[-1] in ['C' , 'c']:
    Fahrenheit = 1.8*(eval(TempStr[0:-1]) + 32)
    print("{:.2f}F".format(Fahrenheit))
else:
    print("Input error.")
