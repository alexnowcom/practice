# class Solution:
def mergeAlternately(word1: str, word2: str) -> str:
    output=""
    w1l=len(word1)
    w2l=len(word2)
    for i in range(0,max(w1l,w2l)):
        if w1l > i:
            output=output + word1[i]
        if w2l > i:
            output=output + word2[i]

    return output
    
print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq"))