

def min_max(nums):
	if len(nums) == 1:
		return (nums[0], nums[0])
	
	(min_num, max_num) = min_max(nums[:-1])
	return (min(min_num, nums[-1]), max(max_num, nums[-1]))


def main():
	nums = [3, 54, -57, -8, 9, 1]
	(min_num, max_num) = min_max(nums)
	print("min:", min_num, "max:", max_num)


if __name__ == "__main__":
    main()
