# Medium (hard) question

# Help from neetcode just conceptual

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        stack = []
        # Added so it become a position, speed pair and sorting 
        for n in range(len(position)):
            arr.append([position[n], speed[n]])
        arr = sorted(arr, reverse=True)
        # Than calculating the time it takes the car to arrive
        # We start from the end so that
        # if the car behind time is smaller or eqaul they become a fleet so we dont push it to stack
        # if the time is bigger than we know it can't catch up to the front car
        for car in arr:
            time = (target - car[0]) / car[1]
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
