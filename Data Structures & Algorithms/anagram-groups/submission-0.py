class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)

        for word in strs:
            baseWord = ''.join(sorted(word))
            anagramList[baseWord].append(word)

        return list(anagramList.values())
        