# This just works for rows and columns
# Also need to find 3x3 for checking duplicates

def isValidSudoku(self, board: List[List[str]]) -> bool:
    col = {}
    for b in board:
        if b[0] == ".":
            continue
        if b[0] in col:
            return False
        col[b[0]] = 1
        row = {}
        for a in b:
            if a == ".":
                continue
            if a in row:
                return False
            row[a] = 1
    return True

# Using a hasmap key as index of col/row/squares value as a set, so that we check if the value exist in the set
# For 3x3 we divide indexes by 3 than set as key pairs such as -> 2,2 -> 2//3, 2//3 = 0,0      3,8 -> 3//3, 8//3 = 1,2

def isValidSudoku(self, board: List[List[str]]) -> bool:
    col = collections.defaultdict(set)
    row = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                continue
            if num in row[i] or num in col[j] or num in squares[(i // 3, j // 3)]:
                return False
            row[i].add(num)
            col[j].add(num)
            squares[(i // 3, j // 3)].add(num)
    return True
