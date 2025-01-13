import random

arr = [3, -57, -8, 54, 9, 1]

def quick_sort(arr, start, stop):
	if start < stop:
		pivot = random_partition(arr, start, stop)
		quick_sort(arr, start, pivot - 1)
		quick_sort(arr, pivot + 1, stop)


def random_partition(arr, start, stop):
	pivot = random.randrange(start, stop)
	arr[start], arr[pivot] = arr[pivot], arr[start]
	return partition(arr, start, stop)


def partition(arr, start, stop):
	pivot = start
	i = start + 1
	for j in range(start + 1, stop + 1):
		if arr[j] <= arr[pivot]:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
	pivot = i - 1
	return pivot




def main():
	quick_sort(arr, 0, len(arr) - 1)
	print(arr)


if __name__ == "__main__":
    main()
