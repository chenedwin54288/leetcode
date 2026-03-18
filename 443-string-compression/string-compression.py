class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars_len = len(chars)
        if chars_len == 1:
            return 1

        current_char = chars[0]
        current_char_start = 0
        current_char_count = 1

        for i in range(1, chars_len):
            #print(i, chars[i], current_char, current_char_count, chars)
            if current_char == chars[i]:
                current_char_count += 1
            
                if i == chars_len - 1:
                    chars[current_char_start] = current_char
                    if current_char_count > 1:
                        str_char_count = str(current_char_count)
                        for j in range(0, len(str_char_count)):
                            chars[current_char_start+1] = str_char_count[j]
                            current_char_start += 1
            else:
                chars[current_char_start] = current_char
                current_char = chars[i]
                if current_char_count > 1:
                    str_char_count = str(current_char_count)
                    for j in range(0, len(str_char_count)):
                        chars[current_char_start+1] = str_char_count[j]
                        current_char_start += 1
                if i == chars_len - 1:
                    chars[current_char_start+1] = current_char

                current_char_count = 1
                current_char_start += 1

                
            #print(i, chars[i], current_char, current_char_count, chars)
        
        chars = chars[:current_char_start+1]
        print(chars)
        return len(chars)




        