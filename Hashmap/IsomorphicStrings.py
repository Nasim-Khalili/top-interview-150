class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s_t = {}
        used_t = set()

        for ch_s, ch_t in zip(s, t):
            if ch_s not in map_s_t:
                if ch_t in used_t:
                    return False
                map_s_t[ch_s] = ch_t
                used_t.add(ch_t)
            else:
                if map_s_t[ch_s] != ch_t:
                    return False

        return True