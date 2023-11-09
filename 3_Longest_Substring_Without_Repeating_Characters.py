#3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occur = {}
        max = 0
        counter = 0
        seq_start = 0
        for i in range(len(s)):
            if s[i] not in last_occur or seq_start > last_occur[s[i]]:
                counter += 1
                last_occur[s[i]] = i
                if counter > max:
                    max = counter
            else:
                counter -= last_occur[s[i]] - seq_start
                seq_start = last_occur[s[i]] + 1
                last_occur[s[i]] = i
        return max
    
#faser than 91.91%, memory less than 98.98%