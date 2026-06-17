class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            key = tuple(count)

            if key not in map:
                map[key] = []
            map[key].append(s)
        return list(map.values())