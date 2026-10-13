class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for st in strs:
            counter = [0]*26
            for ch in st:
                counter[ord(ch)-ord('a')]+=1
            tuple_counter = tuple(counter)
            if tuple_counter not in d:
                d[tuple_counter]=[]
            d[tuple_counter].append(st)
        return list(d.values())