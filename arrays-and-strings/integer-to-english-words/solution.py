class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # consider digits 3 at a time
        # add hundreds to string if valid
        # consider last two digits case by case
        # - 100 > x >= 20: _-ty _
        # - 20 > x >= 13: _-teen
        # - 13 > x: just get names
        # append thousand, million, or billion as necessary
        
        if num == 0:
            return 'Zero'
        
        names = {
            1: 'One ', 2: 'Two ', 3: 'Three ', 4: 'Four ', 5: 'Five ',
            6: 'Six ', 7: 'Seven ', 8: 'Eight ', 9: 'Nine ',
            10: 'Ten ', 11: 'Eleven ', 12: 'Twelve ',
        }
        teens = {
            3: 'Thir', 4: 'Four', 5: 'Fif', 6: 'Six',
            7: 'Seven', 8: 'Eigh', 9: 'Nine',
        }
        tys = {
            2: 'Twen', 3: 'Thir', 4: 'For', 5: 'Fif', 
            6: 'Six', 7: 'Seven', 8: 'Eigh', 9: 'Nine'
        }
        groups = {0: '', 1: 'Thousand ', 2: 'Million ', 3: 'Billion '}
        
        english = ''
        group = 0
        
        while num > 0:
            trip = num % 1000
            
            temp = ''
            if trip > 99:
                temp += names[trip // 100] + 'Hundred '
                
            trip %= 100
            if trip > 0:
                if trip >= 20:
                    temp += tys[trip // 10] + 'ty '
                    trip %= 10
                    if trip > 0:
                        temp += names[trip]
                elif trip >= 13:
                    temp += teens[trip % 10] + 'teen '
                else:
                    temp += names[trip]
            if temp:
                temp += groups[group]
            english = temp + english
            group += 1
            num //= 1000
            
        return english.strip()