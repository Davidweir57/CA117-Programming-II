import sys

def main():
    words = []
    for line in sys.stdin:
        row = [c for c in line.strip()]
        words.append(row)

    col = list(zip(*words))

    col = sorted(["".join(list(tuple)) for tuple in col], key=str.lower)

    sort_rows = list(zip(*col))

    for e in sort_rows:
        print("".join(e))

if __name__ == '__main__':
    main()
