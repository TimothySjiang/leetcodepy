class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return 'Zero'
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        result = ''
        if billion:
            result += self.helper(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += self.helper(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += self.helper(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += self.helper(rest)

        return result

    def helper(self, num):
        dicOne = {
            1: 'One', 2: 'Two', 3: 'Three',
            4: 'Four', 5: 'Five', 6: 'Six',
            7: 'Seven', 8: 'Eight', 9: 'Nine'}

        dicTwo = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
                  14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                  17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        dicTen = {2: 'Twenty', 3: 'Thirty', 4: 'Forty',
                  5: 'Fifty', 6: 'Sixty', 7: 'Seventy',
                  8: 'Eighty', 9: 'Ninety'}

        hundred = num // 100
        ten = (num - hundred * 100) // 10
        rest = num - hundred * 100 - ten * 10

        result = ''
        if hundred:
            result += dicOne[hundred] + ' Hundred'
        if ten:
            result += ' ' if result else ''
            if ten * 10 + rest < 20:
                result += dicTwo[ten * 10 + rest]
                return result
            else:
                result += dicTen[ten]
        if rest:
            result += ' ' if result else ''
            result += dicOne[rest]
        return result