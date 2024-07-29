# helps define a condition

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# using the tenary operator
def is_adult2(age):
    return True if age > 18 else False

print(is_adult(12))
print(is_adult2(45))