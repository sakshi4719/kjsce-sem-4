def selection_sort(nums):
	for i in range(len(nums)):
		min = i
		for j in range(i, len(nums)):
			if(nums[j] < nums[min]):
				min = j
		if(i != min):
			(nums[i], nums[min]) = (nums[min], nums[i])
	return nums


def main():
	nums = [3, 54, -57, -8, 9, 1]
	sorted_nums = selection_sort(nums)
	print(sorted_nums)

if __name__ == '__main__':
	main()
