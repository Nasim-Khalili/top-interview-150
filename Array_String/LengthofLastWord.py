class Solution(object):
    def lengthOfLastWord(self, s):
        
        s = s.rstrip()

        words = s.split(' ')

        return len(words[-1])