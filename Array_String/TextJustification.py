class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0 

        while i < len(words):
            
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1


            line = ''
            num_words = j - i
            
            if j == len(words) or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                space_between_words = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    
                    spaces_to_add = space_between_words + (1 if k - i < extra_spaces else 0)
                    line += ' ' * spaces_to_add

                line += words[j - 1]

            res.append(line)
            i = j

        return res
