def insertion_sort(nums, n):
	if n <= 1:
		return nums

	insertion_sort(nums, n - 1)
	
	key = nums[n - 1]
	j = n - 2
	
	while j >= 0 and nums[j] > key:
		nums[j + 1] = nums[j]
		j -= 1
	nums[j + 1] = key
	return nums

	


def main():
	nums = [3, 54, -57, -8, 9, 1]
	print(insertion_sort(nums, len(nums)))


if __name__ == "__main__":
    main()
