#This code is taken from https://www.youtube.com/watch?v=Ph95IHmRp5M 
#This is NOT my original work

def solveNQueens(n):
    col = set()
    posDiag = set()
    negDiag = set()
    res = []
    board = [["."]*n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            print(copy)
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            print("The value of r is now: ", (r +1))
            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
    backtrack(0)
    return res

def main():
    solveNQueens(4)

if __name__ == "__main__":
    main()