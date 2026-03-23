class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ele_dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in ele_dict:
                ele_dict[nums[i]] = 0
            ele_dict[nums[i]] += 1
        
        dict_list = list(ele_dict.items())
        print(dict_list)
        def get_count(e):
            return e[1]
        dict_list.sort(key=get_count)
        return_list = []
        for j in range (len(dict_list)-1, len(dict_list)-1-k, -1):
            return_list.append(dict_list[j][0])

        return return_list
        

        