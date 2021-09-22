public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        // Because the Java don't have thing like unsinged type
        // In Java, the compiler represents the signed integers using 2's complement notation.
        // Concept is the same:
        // Loop 32 times:->problem state that 32bit integer.
        // result is shift to the left 1 bits
        // if the right most bit in number is 1 -> plus 1 to the result
        // shift the number to the right 1 bits, because we done with that right most bit.
        // return result
        // Time O(n)
        // Space O(1)
        int result = 0;
        for (int i=0; i<=31; i++){
            result = result << 1;
            if ((n&1)==1){
                result = result + 1;
            }
            n = n>>1;
        }
        return result;
    }
}