class Node():
    def __init__(self):
        self.dic = {}
        self.isFile = False
        self.Filename = ''
        self.content = ''

class FileSystem:
    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        node = self.root
        path = path.split('/')
        for d in path:
            if d:
                if d not in node.dic:
                    return []
                node = node.dic[d]
        if node.isFile:
            return [node.Filename]
        return sorted(node.dic.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        path = path.split('/')
        for d in path:
            if d:
                if d not in node.dic:
                    node.dic[d] = Node()
                node = node.dic[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        path = filePath.split('/')
        self.mkdir(filePath)
        for d in path:
            if d:
                node = node.dic[d]
        node.isFile = True
        node.content += content
        node.Filename = d

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        path = filePath.split('/')
        for d in path:
            if d:
                node = node.dic[d]
        return node.content


        # Your FileSystem object will be instantiated and called as such:
        # obj = FileSystem()
        # param_1 = obj.ls(path)
        # obj.mkdir(path)
        # obj.addContentToFile(filePath,content)
        # param_4 = obj.readContentFromFile(filePath)