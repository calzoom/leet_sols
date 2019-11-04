from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if s == "":
            return ""
        
        if t == "":
            return ""

        # hash to track characters in t 
        t_char = Counter()
        for c in t:
            t_char[c] += 1

        t_len = len(set(t))

        # initialize two ptr to start of string and begin sliding window
        beg_ptr = 0
        end_ptr = -1

        # dict with valid_substring as key and length as value
        valid = {}
        valid[""] = len(s) + 1 # if we aren't able to find a valid match return ""

        while beg_ptr <= (len(s) - len(t)):
            while t_len != 0:
                end_ptr += 1
                if end_ptr >= len(s):
                    # t_len != 0 and end_ptr has reached the end
                    return min(valid, key=valid.get) # argmin valid dictionary
                if s[end_ptr] in t:
                    t_char[s[end_ptr]] -= 1
                    if t_char[s[end_ptr]] == 0:
                        t_len -= 1

            # at this point we have  a valid substring of s containing all of t, 
            # parameterized by beg_ptr and end_ptr 
            valid[s[beg_ptr:end_ptr + 1]] = end_ptr - beg_ptr   # store the substring and its length

            # # the substring is lower bounded by len(t)
            # if (end_ptr - beg_ptr) - 1 == len(t): 
            #     return s[beg_ptr:end_ptr + 1]

            if s[beg_ptr] in t:
                t_char[s[beg_ptr]] += 1 # we are losing a character 
                if t_char[s[beg_ptr]] > 0:
                    t_len += 1  # losing a character from minimum validity guarantees the counter to be >= 1
                beg_ptr += 1

            if beg_ptr >= len(s):
                    return min(valid, key=valid.get)

            # to find a smaller substring if we lose a beg_ptr we have to start at another char start in t
            # only enter this while loop if the prev condition was failed
            while s[beg_ptr] not in t:
                beg_ptr +=1 
                if beg_ptr >= len(s):
                    return min(valid, key=valid.get)
    
        return min(valid, key=valid.get)