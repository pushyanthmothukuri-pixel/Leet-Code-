class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
     
        if not strs:
            return ""
        
        
        strs.sort()
   
        first_string = strs[0]
        last_string = strs[-1]
        
        
        prefix_length = 0
        while prefix_length < len(first_string) and prefix_length < len(last_string):
            if first_string[prefix_length] == last_string[prefix_length]:
                prefix_length += 1
            else:
                break
                
      
        return first_string[:prefix_length]