from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)
        for s in strs:
            sign= "".join(sorted(s))
            groups[sign].append(s)
        return list(groups.values())