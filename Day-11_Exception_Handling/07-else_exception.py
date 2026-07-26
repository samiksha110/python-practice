# else

try:
    x = 20
    y = 5

    print(x / y)     # 20/5 = 4.0 

except ZeroDivisionError:
    print("Error")   # Skipped because no exception occurred

else:
    print("Success")  # Executes because try completed successfully
