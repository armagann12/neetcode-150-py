class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        for c in magazine:
            hashMap[c] = hashMap.get(c, 0) + 1

        for char in ransomNote:
            if hashMap.get(char, 0) <= 0:
                return False
            hashMap[char] -= 1
        return True
