class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] 

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        arr = self.store[key]

        left = 0
        right = len(arr) - 1

        answer = ""

        while left <= right:

            mid = (left + right) // 2

            mid_timestamp = arr[mid][0]
            mid_value = arr[mid][1]

            if mid_timestamp <= timestamp:
                answer = mid_value
                left = mid + 1

            else:
                right = mid - 1

        return answer

        


    