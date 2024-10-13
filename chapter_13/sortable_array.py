class SortableArray:

    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot = self.array[pivot_index]

        right_pointer -= 1

        while True:

            while self.array[left_pointer] < pivot:
                left_pointer += 1

            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = \
                    self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1

        self.array[left_pointer], self.array[pivot_index] = \
            self.array[pivot_index], self.array[left_pointer]

        return left_pointer
    def quicksort(self, left_index, right_index):
        if right_index - left_index <= 0:
            return

        pivot_index = self.partition(left_index, right_index)

        self.quicksort(left_index, pivot_index - 1)

        self.quicksort(pivot_index + 1, right_index)
    def quickselect(self, kth_lowest_value, left_index, right_index):
        if right_index - left_index <= 0:
            return self.array[left_index]

        pivot_index = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            return self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            return self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.array[pivot_index]
