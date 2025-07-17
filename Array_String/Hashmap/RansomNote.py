class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashmap = {}

        for char in magazine:
            hashmap[char] = hashmap.get(char, 0) + 1

        for char in ransomNote:
            if hashmap.get(char, 0) == 0:
                return False
            hashmap[char] -= 1

        return True