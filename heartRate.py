"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.

This program calculates the slowest and fastest heart rates necessary to strengthen a person's heart.
"""

# Get the person's age
age = int(input("Please enter your age: "))

# Calculate the slowest and fastest heart rates
slowest_rate = (220 - age) * 0.5
fastest_rate = (220 - age) * 0.85

# Print the slowest and fastest heart rates
print("When you exercise to strengthen your heart, you should keep your heart rate between")
print(slowest_rate, "and", fastest_rate, "beats per minute.")   