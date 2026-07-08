class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        index1 = 0
        index2 = n - 1

        while index1<index2:
            current = numbers[index1] + numbers[index2]
            if current> target:
                index2 -= 1

            elif current < target:
                index1 += 1

            else:
                return [index1+1, index2+1]
            