# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 
# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

def reverseVowels(s: str) -> str:
    result="" # " " * len(s)}
    holder={}
    vowels={}
    flipped_vowels=[]

    print(s)

    position=0
    for char in s:
        if char in ['a','A','e','E','i','I','o','O','u','U']:
            vowels[position] = char
        else:
            holder[position] = char
        position = position + 1

    print(holder)
    print(vowels)

    for vowel in vowels:
        flipped_vowels.append(vowels[vowel])
    flipped_vowels.reverse()

    print(flipped_vowels)

    i = 0
    for pos, vowel in vowels.items():
        holder[pos] = flipped_vowels[i]
        i = i + 1

    print(holder)

    for letter in sorted(holder):
         result = result + holder[letter]

    return result

print(reverseVowels('hello'))
print(reverseVowels('leetcode'))
print(reverseVowels('aA'))