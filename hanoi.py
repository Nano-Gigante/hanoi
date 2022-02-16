class hanoi:

    def __init__(self,n,vb=False):
        self.pn = n
        self.board = [[self.pn - x for x in range(self.pn)] , [] , []]
        self.moves = 0
        self.verbose = vb
    

    #finds a disk
    def locate(self,n):
        for i in range(3):
            if n in self.board[i]:
                return i

    #prints the self.board
    def printt(self):
        for i in range(self.pn):
            for stack in self.board:
                try:
                    print(stack[self.pn-i-1], end='')
                except:
                    print(".",end='')
                print("  ",end='')
            print()
        print("-------\n")

    #moves the top disk from source to dst if possible
    def move(self,src,dst):
        if len(self.board[src]) == 0:
            return
        if len(self.board[dst]) == 0 or self.board[dst][-1] > self.board[src][-1]:
            if self.verbose:
                print(f'moving {self.board[src][-1]} to {dst+1}')
                self.printt()
            self.board[dst].append(self.board[src].pop())
            self.moves+=1


    #checks if there are problems with a move
    #if there are it returns a move that fixs the problem
    def obs(self,n,dst) -> list:
        src = self.locate(n)
        ris = None
        
        if self.board[src][-1] != n:
            top = self.board[src][self.board[src].index(n)+1:][0]
            ris = [ top , 3 - src - dst]
        else:
            for i in self.board[dst]:
                if i < n:
                    ris = [ i , 3 - dst - src ]
                    break
        
        if self.verbose :
            print(f'attempting {n} -> {dst+1}')
            if ris is None:
                print('move is fine')
            else:        
                print(f'problem found, fix {ris[0]} -> {ris[1]+1}')
            print()

        return ris
        
    #recursive mover 
    def rec_move(self,n,dst):
        o = self.obs(n,dst)

        if self.locate(n) == dst:
            return

        while o is not None:
            self.rec_move(o[0],o[1])
            o = self.obs(n,dst)
        
        self.move(self.locate(n),dst)

    def solve(self):
        for i in range(self.pn):
            self.rec_move(self.pn-i,2)

        print(f'solved in {self.moves} moves')

if __name__ == '__main__':
    h = hanoi(5,True)
    h.solve()