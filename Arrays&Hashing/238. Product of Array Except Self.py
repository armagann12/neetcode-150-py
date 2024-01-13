# Brute Force

def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(len(answer)):
            if not i == j:
                answer[j] *= nums[i]
    return answer


# Prefix and Postfix -> Needs Refactoring

def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix, postfix, answer = [1] * len(nums), [1] * len(nums), [1] * len(nums)
    prefix[0] = nums[0]
    postfix[-1] = nums[-1]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i]
    for i in range(len(nums) - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i]
    for i in range(len(answer)):
        # This part needs refactoring
        if i == 0:
            pre = 1
        else:
            pre = prefix[i - 1]
        if i == len(nums) - 1:
            post = 1
        else:
            post = postfix[i + 1]
        answer[i] = pre * post
    return answer
