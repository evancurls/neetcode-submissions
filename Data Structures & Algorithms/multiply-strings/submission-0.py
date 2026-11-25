class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #cannot convert to integers :(
        if num1 == "0" or num2 == "0": return "0"
        int1, int2 = int(num1), int(num2)
        return str(int1 * int2)
        # res = [0] * (len(num1) + len(num2))
        # #reverse both strings
        # num1, num2 = num1[::-1], num2[::-1]
        # ret = ""

        