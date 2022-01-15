class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        
        if num // 1000 >= 1:
            rep = num // 1000
            ans = ans + 'M'*rep
            num -= 1000*rep
        if num - 900 < 100 and num >= 900:
            ans = ans + 'CM'
            num -= 900
        if num - 400 < 100 and num >= 400:
            ans = ans + 'CD'
            num -= 400
        if num // 500 >= 1:
            rep = num // 500
            ans = ans + 'D'*rep
            num -= 500*rep
        if num // 100 >= 1:
            rep = num // 100
            ans = ans + 'C'*rep
            num -= 100*rep
        if num - 90 < 10 and num >= 90:
            ans = ans + 'XC'
            num -= 90
        if num - 40 < 10 and num >= 40:
            ans = ans + 'XL'
            num -= 40
        if num // 50 >= 1:
            rep = num // 50
            ans = ans + 'L'*rep
            num -= 50*rep
        if num // 10 >= 1 :
            rep = num // 10
            ans = ans + 'X'*rep
            num -= 10*rep
        if num == 9:
            ans = ans + 'IX'
            num -= 9
        if num == 4:
            ans = ans + 'IV'
            num -= 4
        if num // 5 >= 1:
            rep = num // 5
            ans = ans + 'V'*rep
            num -= 5*rep
        ans = ans + 'I' *num
            
            
        return ans