function reverse(arr){
    for(i=0; i < arr.length; i++){
        arr[i] = arr[arr.length-1] - arr[i];
        arr[i]++;
    }
    return arr;
}
console.log(reverse(1,3,4,2,5));