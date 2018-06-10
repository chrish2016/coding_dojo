var arr = [2,4,6,8];
console.log(arr);

arr[1] = 10;
console.log(arr);

var temp = arr[1];
arr[1] = arr[3];
arr[3] = temp;
console.log(arr);