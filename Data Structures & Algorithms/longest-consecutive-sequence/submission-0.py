class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest_num_count = 0

        for num in number_set:
            if (num - 1) not in number_set:
                current_num = num
                current_num_count = 1

                while (current_num +1) in number_set:
                    current_num += 1
                    current_num_count +=1

                longest_num_count = max(longest_num_count, current_num_count)
        return longest_num_count 