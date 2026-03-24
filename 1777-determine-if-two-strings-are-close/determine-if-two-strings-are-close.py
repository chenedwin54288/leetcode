class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # # check length same
        # if len(word1) != len(word2):
        #     return False
        
        # # apply op1 many times
        # word1 = sorted(word1)
        # word2 = sorted(word2)
        # if word1 == word2:
        #     return True

        # # make a map so that op2 can be applied
        # word1_map = {}
        # word2_map = {}
        # for i,j in zip(word1, word2):
        #     word1_map[i] = 1 + word1_map.get(i, 0)
        #     word2_map[j] = 1 + word2_map.get(j, 0)

        
        # freq_list2 = []
        # for cr2, target_ct2 in word2_map.items():
        #     if cr2 in word1_map:
        #         # for cr1, target_ct1 in word1_map.items():
        #         #     if target_ct2 == target_ct1:
        #         #         temp = word1_map[cr2] 
        #         #         word1_map[cr1] = temp
        #         #         word1_map[cr2] = target_ct1
        #         freq_list2.append(target_ct2)
        #     else:
        #         return False

        # if sorted(list(word1_map.values())) != sorted(freq_list2):
        #     # print(word1_map, word2_map)
        #     return False
        
        # return True
        if len(word1) != len(word2):
            return False
        
        # Count frequencies
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        # Rule 1: Must have the same unique characters
        # Using set() or checking keys() works here
        if set(c1.keys()) != set(c2.keys()):
            return False
            
        # Rule 2: The frequencies themselves must be the same 
        # (e.g., if one has frequencies 3, 2, 1, the other must too)
        return sorted(c1.values()) == sorted(c2.values())

        

        
        