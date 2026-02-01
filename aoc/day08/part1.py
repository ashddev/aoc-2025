import math, heapq, json
from pprint import pprint
from typing import Callable

f = open("./input.txt")
inputtxt = f.read()
f.close()


class ClosestPoints:
    def __init__(self, k: int):
        self.K = k
        self.heap = []
        self.seen = set()
        heapq.heapify(self.heap)

    def add_pair(self, pair, distance):
        key = json.dumps(sorted(pair))
        if key not in self.seen:
            if len(self.heap) < self.K:
                heapq.heappush(self.heap, (-distance, pair))
            else:
                if distance < -self.heap[0][0]:
                    heapq.heapreplace(self.heap, (-distance, pair))

    def get(self):
        return sorted([(-d, x) for (d, x) in self.heap])


def distance(p: list[int], q: list[int]) -> float:
    return math.sqrt(sum([math.pow(q_i - p_i, 2) for p_i, q_i in zip(p, q)]))


def solve(input: str):
    transform: Callable[[str], list[int]] = lambda p: list(
        map(int, p.strip().split(","))
    )
    points = [transform(p) for p in input.strip().split("\n")]
    cp = ClosestPoints(10)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            cp.add_pair((points[i], points[j]), d)
    pprint(cp.get())


print(solve(inputtxt))
