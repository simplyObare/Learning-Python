# Dictionaries
band = {
   "vocals" : "Plant",
   "guitar" : "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band))

# Accessing items
print(band["vocals"])
print(band.get("guitar"))


# List all keys
print(band.keys())

# Print all values
print(band.values())