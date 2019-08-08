class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        if not paths:
            return []

        files = collections.defaultdict(list)
        for path in paths:
            root, *f = path.split(" ")

            for file in f:
                txt, content = file.split("(")
                content = content[:-1]
                files[content].append(root + "/" + txt)

        return [files[key] for key in files if len(files[key]) > 1]