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
