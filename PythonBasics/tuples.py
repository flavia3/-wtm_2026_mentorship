# 5. Days of the Week 
days_of_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print(days_of_week)

print(f"The first day of the week is {days_of_week[0]}")

print(f"The last day of the week is {days_of_week[-1]}")


days_of_week[0] = "Sunday"
print(days_of_week)
# TypeError: 'tuple' object does not support item assignment
# The program produces a TypeError because tuples are immutable. This means when a tuple is created, its values cannot be changed, added, or removed.

# A tuple is different from a list because a tuple is immutable, while a list is mutable.