print(20 * 24 * 60 ) # 8640
print(20 * 24 * 60 * 60) # 86400
print(20 * 24 * 60 * 60 + 12 * 60 * 60) # 95040
print(20 * 24 * 60 * 60 + 12 * 60 * 60 + 30 * 60) # 95080
print(20 * 24 * 60 * 60 + 12 * 60 * 60 + 30 * 60 + 15) # 95115
# Explanation:
# The expression 20 * 24 * 60 * 60 represents the number of seconds in a day.
# Adding 12 hours * 60 minutes * 60 seconds to it gives us the number of seconds in a day + 12 hours.
# Similarly, adding 30 minutes * 60 seconds to it gives us the number of seconds in a day + 12 hours + 30 minutes.
# Finally, adding 15 seconds to it gives us the total number of seconds in a day + 12 hours + 30 minutes + 15 seconds.
# This is equivalent to the number printed after the expression.