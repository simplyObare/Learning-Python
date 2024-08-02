tries = 0
code = ''

while tries < 5 and code != 'python':
   code = input('Enter programming language: ').lower()
   tries += 1
   
if code == 'python':
   print(f"It took you {tries} tries")