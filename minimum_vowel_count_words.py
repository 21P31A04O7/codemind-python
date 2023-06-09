string=input().split()
vowel_count=[sum(char.lower() in 'aeiou'for char in word)for word in string]
min_vowels=min(vowel_count)
word_count=vowel_count.count(min_vowels)
print(word_count)