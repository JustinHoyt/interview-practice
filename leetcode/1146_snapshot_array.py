def binary_search(arr: list[list[int]], target: list[int]):
    low_idx = 0
    hi_idx = len(arr)
    while low_idx < hi_idx:
        mid_idx = (low_idx + hi_idx) // 2
        if target <= arr[mid_idx]:
            hi_idx = mid_idx
        else:
            low_idx = mid_idx + 1

    return low_idx


class SnapshotArray:

    def __init__(self, length: int):
        SnapList = list[list[list[int]]]
        self.list: SnapList = []
        self.snap_id = -1
        for _ in range(length):
            self.list.append([[-1, 0]])


    def set(self, index: int, val: int) -> None:
        self.list[index].append([self.snap_id, val])


    def snap(self) -> int:
        self.snap_id += 1
        for row in self.list:
            row[-1][0] = self.snap_id

        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        row = self.list[index]
        snap_idx = binary_search(row, [snap_id])
        _, val = row[snap_idx]
        return val


def test_happy_path():
    snapshotArr = SnapshotArray(3)
    snapshotArr.set(index=0, val=5)                  # Set array[0] = 5
    snapshotArr.snap()                               # Take a snapshot, return snap_id = 0
    snapshotArr.set(index=0, val=6)
    assert snapshotArr.get(index=0, snap_id=0) == 5  # Get the value of array[0] with snap_id = 0, return 5
    assert snapshotArr.get(index=1, snap_id=0) == 0  # Get the value of array[0] with snap_id = 0, return 5

    snapshotArr.snap()
    assert snapshotArr.get(index=0, snap_id=0) == 5  # Get the value of array[0] with snap_id = 0, return 5
    assert snapshotArr.get(index=0, snap_id=1) == 6  # Get the value of array[0] with snap_id = 0, return 5

    snapshotArr.snap()
    assert snapshotArr.get(index=0, snap_id=1) == 6  # Get the value of array[0] with snap_id = 0, return 5
    assert snapshotArr.get(index=0, snap_id=2) == 6  # Get the value of array[0] with snap_id = 0, return 5





if __name__ == "__main__":
    test_happy_path()
