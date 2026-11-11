class Solution:
    def reverse(self, x: int) -> int:
        set_x = str(x)

        if x < 0:
            set_x = set_x[::-1]
            set_x = set_x[:-1]

            #print(set_x)
        else:
            set_x = set_x[::-1]
            #print(set_x)
        
        int_x = int(set_x)
        if int_x > (2 ** 31) - 1: return 0
        if x < 0:
            int_x *= -1

        return int_x      