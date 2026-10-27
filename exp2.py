grid = [
    ['S','.','#'],
    ['#','.','.'],
    ['.','.','G']
]

visited = set()

def move(r,c):
    if(r,c) in visited or grid[r][c] == '#':
        return False

    visited.add((r,c))
    print(f"Visiting: ({r},{c})")

    if grid[r][c] == 'G':
        print("Goal reached!")
        return True

    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = r+dr , c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            if move(nr,nc):
                return True

    return False

move(0,0)