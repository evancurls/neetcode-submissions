class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t temp = n;
        int sum = 0;
        for (uint32_t i = pow(2, 31); i > 0; i /= 2){
            sum += temp / i;
            temp = temp % i;
        }
        return sum;

    }
};
