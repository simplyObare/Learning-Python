vowels = 'aeiou'
const = 'bcdfghjklmnpqrstvwxyz'

word = input('Enter a word: ')
vowel_num = 0
for letter in word:
   if letter in vowels:
      vowel_num += 1
   elif letter in const:
    vowel_num += 0
    
print(f'Number of vowels: {vowel_num}')