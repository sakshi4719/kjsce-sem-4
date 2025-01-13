nums = [3, 54, -57, -8, 9, 1]

def min_index(nums, i, j):
	if i == j:
		return i
	
	min = min_index(nums, i+1, j)

	if nums[i] < nums[min]:
		return i
	return min


def selection_sort(nums, i):
	if i == len(nums):
		return -1

	min = min_index(nums, i, len(nums)-1)
	
	if(min != i):
		(nums[i], nums[min]) = (nums[min], nums[i])
	
	selection_sort(nums, i+1)


def main():
	selection_sort(nums, 0)
	print(nums)


if __name__ == "__main__":
    main()
