class Solution:
    # Turning array into one string where its stored in the string as 
    # first the length of the word than # than the word:
    # Ex. 3#arm5#baris4#mami
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # Turning the string into array using the length of the words using indexes
    # to take them and append them to the result array
    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
    
res = Solution()
arr = ["arm", "baris", "mami"]
encoded = res.encode(arr)
print(encoded, "- Encoded")
decoded = res.decode(encoded)
print(decoded, "- Decoded")