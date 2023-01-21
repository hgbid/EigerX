#include <stdio.h>

int  recursiveSum(int number, int sum){
    // the function gets a number and return the sum of it's digits
    if (number == 0)
        return sum;
    return recursiveSum(number/10, sum + number % 10);
}

int digitSum(int number){
    // initialize sum of digit to zero and call recursiveSum
    return recursiveSum(number, 0);
}

int main() {
    int number = 2347623;
    int ans = digitSum(2347623);
    printf("Number: %d > Sum of digits: %d",number, ans);
    return 0;
}
