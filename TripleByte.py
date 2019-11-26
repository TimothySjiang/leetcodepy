class Spreadsheet():
    def __init__(self,row,col):
        self.sheet = [[''] * col for i in range(row)]
        self.length = [0] * col

    def update(self,i,j,val):
        self.sheet[i][j] = str(val)
        self.length[j] = 0
        for i in range(len(self.sheet)):
            self.length[j] = max(self.length[j],len(self.sheet[i][j]))

    def print(self):
        r, c = len(self.sheet), len(self.sheet[0])
        for i in range(r):
            for j in range(c):
                if j != c-1:
                    print(self.sheet[i][j].ljust(self.length[j]) + '|', end = '')
                else:
                    print(self.sheet[i][j].ljust(self.length[j]))

if __name__ == '__main__':
    test = Spreadsheet(4,3)
    test.update(0,0,'bob')
    test.update(0,1,10)
    test.update(0,2,'foo')
    test.update(1,0,'alice')
    test.update(1,1,5)
    test.print()
    test.update(1,0,'a')
    test.print()
