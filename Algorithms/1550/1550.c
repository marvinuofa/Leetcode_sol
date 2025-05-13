int threeConsecutiveOdds(int* arr, int arrSize) {
    int count = 0;  // Counter to track consecutive odd numbers

    // Loop through each element in the array
    for(int i = 0; i < arrSize; i++){
        if ((arr[i] % 2) == 1){ 
            // If current element is odd, increment counter
            count += 1; 
        }
        else{
            // If it's even, reset the counter
            count = 0;
        }

        // If we've seen three consecutive odds, return true (1)
        if (count == 3){
            return 1;
        }
    }

    // No three consecutive odd numbers found
    return 0; 
}
