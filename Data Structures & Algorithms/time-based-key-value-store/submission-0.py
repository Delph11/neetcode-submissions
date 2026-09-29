class TimeMap:

    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))  # timestamps are strictly increasing

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        lst = self.store[key]
        lo, hi = 0, len(lst) - 1
        ans = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if lst[mid][0] <= timestamp:
                ans = lst[mid][1]   # valid candidate, try to find a later one
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
