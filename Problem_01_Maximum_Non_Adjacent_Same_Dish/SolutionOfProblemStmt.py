class solution:
    def dish(self,n,nums):
        type = set(nums)
        bestType = None
        bestCount = -1

        for t in type:
            count = 0
            lastTaken = -2
            for i in range(n):
                if nums[i] == t and i != lastTaken + 1:
                    count += 1
                    lastTaken = i

            if count > bestCount or (count == bestCount and (bestType is None or t < bestType)):
                bestCount = count
                bestType = t

        return bestType

T = int(input())

for _ in range(T):
    n = int(input())
    nums = list(map(int,input().split()))

    sol = solution()
    print(sol.dish(n,nums))
