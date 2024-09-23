g = lambda x: 3 * x + 1
print(g(3))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("john", "smith"))


scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Arthur C. Clarke", "Douglas Adams", "George Orwell", "Kurt Vonnegut", "Philip K. Dick", "Ursula K. Le Guin", "Octavia Butler", "China Mieville", "Iain M. Banks", "Cixin Liu"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)