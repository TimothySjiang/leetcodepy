class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        #define a DFA
        state = [{},
                {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                {'digit':3,'.':4},
                {'digit':3,'e':5,'.':6},
                {'digit':6},
                {'digit':7,'sign':8},
                {'e':5,'digit':6},
                {'digit':7},
                {'digit':7},
                ]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        print(currentState)
        if currentState not in [3,6,7]:
            return False
        return True