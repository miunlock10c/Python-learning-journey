try:
    number = int(input("Enter a number : "))
    print(10 / number)

# except ZeroDivisionError:
#    print("ZeroDivisionError")
#    print("Dont enter zero")
#
# except ValueError:
#    print("Error of ValueError")
#    print("Bro enter a number")

except Exception as error:
    print(f'Error is {error}')

else:
    print("Error has not been detected")

finally:
    print("this text will prints every possible situation")
