class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = list(str(x))
        if xs[0] == '-':
            return False
        half = len(xs) //2 + 1
        pre = xs[:half]
        pst = xs[-half:]
        print(pre)
        print(pst)
        
        if pre == pst[::-1]:
            return True
        return False
        