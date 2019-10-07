class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        prefix = collections.defaultdict(list)
        suffix = collections.defaultdict(list)
        res = set()
        for phrase in phrases:
            ph = phrase.split()
            start = ph[0]
            end = ph[-1]
            if start in suffix:
                tmp = {x + phrase[len(start):] for x in suffix[start]}
                res |= tmp
            if end in prefix:
                tmp = {phrase + x[len(end):] for x in prefix[end]}
                res |= tmp
            prefix[start].append(phrase)
            suffix[end].append(phrase)

        return sorted(list(res))