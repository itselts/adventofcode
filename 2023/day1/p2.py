with open('input.txt') as f:
    sum = 0
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for line in f.read().splitlines():
        digits = []
        for i,c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for num in nums:
                if line[i:].startswith(num):
                    digits.append(nums[num])
        sum += int(digits[0]+digits[-1])
    print(sum)

            