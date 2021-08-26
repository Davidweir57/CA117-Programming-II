import sys
from priority_queue_112 import PQ

def main():

    m = int(sys.argv[1])
    pq = PQ()

    for line in sys.stdin:
        pq.insert(int(line.strip()))

        while pq.size() > m:
            pq.delMax()

    while pq.is_empty() is False:
        print(pq.delMax())

if __name__ == '__main__':
    main()
