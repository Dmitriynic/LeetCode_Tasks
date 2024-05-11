# 383 Ransom Note

#simple solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)
        for elem in magazine:
            dict_2[elem] += 1
        for elem in ransomNote:
            dict_1[elem] += 1
        for key, value in dict_1.items():
            if dict_2[key] < value:
                return False
        return True
#faster than 66.25%, memory less than 46.05%

#counter solution
class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
#faster than 62.86%, memory less than 46.05%
