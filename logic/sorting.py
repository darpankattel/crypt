class Sort:
    def __init__(self, sorting_option_config) -> None:
        self.sorting_option_config = sorting_option_config

    def quick_sort(self, arr, left, right):
        if left < right:
            pivot = self.partition(arr, left, right)
            self.quick_sort(arr, left, pivot - 1)
            self.quick_sort(arr, pivot + 1, right)

    def partition(self, arr, left, right):
        if self.sorting_option_config["sort_by"] == "name":
            pivot_value = arr[right].name
        else:
            pivot_value = arr[right].created

        i = left - 1
        for j in range(left, right):
            if self.sorting_option_config["sort_by"] == "name":
                compare_value = arr[j].name.lower()
            else:
                compare_value = arr[j].created

            if (self.sorting_option_config["order"] == "ascending" and compare_value <= pivot_value) or (self.sorting_option_config["order"] == "descending" and compare_value >= pivot_value):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
