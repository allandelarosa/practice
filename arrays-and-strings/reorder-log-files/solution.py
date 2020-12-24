class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        def cmp_items(log1, log2):
            log1 = log1.split()
            log2 = log2.split()
            
            for a, b in zip(log1[1:], log2[1:]):
                if a > b:
                    return 1
                if a < b:
                    return -1
            
            if log1[0] > log2[0]:
                return 1
            if log1[0] < log2[0]:
                return -1
            return 0
        
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(cmp_items)
        
        return letter_logs + digit_logs