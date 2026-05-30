class TimeMap:

    def __init__(self):
        # key list of [timestamp, value]
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps come in adding order so just append
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # if key does not exist return ""
        if key not in self.store:
            return ""

        values = self.store[key]
        left = 0
        right = len(values) - 1
        res = ""

        while left <= right:
            mid = (left+right) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res

