dirs = [(0,1),(1,0),(0,-1),(-1,0)] # 当前位置四个方向上的偏移量
path = [] # 找到的路径
def mark(maze, pos): # 给迷宫maze的位置pos标“2”表示“到过了”
    maze[pos[0]][pos[1]] = 2
def passable(maze, pos): # 检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ") # 已到达出口，输出这个位置。成功结束
        path.append(pos)
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] +dirs[i][1]
        # 考虑下一个可能的方向
        if passable(maze, nextp): # 不可行的相邻位置不用管
            if find_path(maze, nextp, end):
                # 如果从nextp可达出口，输出这个位置。成功结束
                print(pos, end=" ")
                path.append(pos)
                return True
    return False
def see_path(maze, path): # 使找到的路径可视化
    for i, p in enumerate(path):
        if i == 0:
            maze[p[0]][p[1]] == "E"
        elif i == len(path) -1:
            maze[p[0]][p[1]] == "S"
        else:
            maze[p[0]][p[1]] == 3
    print("\n")
    for r in maze:
        for c in r:
            if c == 3:
                print('\033[0;31m' + "*" + " " + '\033[0m', end="")
            elif c == "S" or c == "E":
                print('\033[0;34m' + c + " " + '\033[0m', end="")
            elif c == 2:
                print('\033[0;32m' + "#" + " " + '\033[0m', end="")
            elif c == 1:
                print('\033[0;;40m' + " " *2 + '\033[0m', end="")
            else:
                print(" "*2, end="")
        print()

if __name__ == '__main__':
    maze =[ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1], \
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], \
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], \
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1], \
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], \
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], \
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], \
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1], \
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1], \
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    ]
    start =(1,1)
    end = (10,12)
    find_path(maze, start, end)
    see_path(maze, path)