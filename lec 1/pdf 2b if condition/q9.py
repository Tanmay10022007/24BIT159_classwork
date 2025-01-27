a=int(input("enter integer"))
if a < 0:
    absolute_value = -a  # Negate the number if it's negative
else:
    absolute_value = a  # Keep the number as-is if it's non-negative

print("The absolute value of", a, "is", absolute_value)