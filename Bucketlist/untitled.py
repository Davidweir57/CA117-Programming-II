#!/usr/bin/env python3

import sys

def stars(lines, numl, numc):
    starlist = []
    for rows in range(0, int(numl)):
        for col in range(0, int(numc)):
            if lines[rows][col] == "-":
                starlist.append([rows, col])
    return starlist

def numstars(grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '-':
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '-':
        return
    grid[i][j] = '#'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)

def main():
    s = sys.stdin.readline().split()
    numl = s[0]
    numc = s[1]

    lines = []
    for line in sys.stdin:
        line = line.strip()
        line = [c for c in line]
        lines.append(line)

    # starlist = stars(lines, numl, numc)
    count = numstars(lines)
    print(count)

if __name__ == '__main__':
    main()
