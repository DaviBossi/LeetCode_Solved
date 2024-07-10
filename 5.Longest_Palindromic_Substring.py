class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                aux = s[i:j]
                if aux == aux[::-1] and len(aux) > len(ans):
                    ans = aux 
        
        return ans
        

        
                


        