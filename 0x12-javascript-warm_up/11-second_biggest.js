#!/usr/bin/node
const args = process.argv.slice(2);
// create the findSecondMax()
function findSecondMax (arr) {
  // initialize the maximum and second max to smallest possible number
  let max = -Infinity;
  let secondMax = -Infinity;
  // loop through the array
  for (let i = 0; i < arr.length; i++) {
    const val = parseInt(arr[i]);
    // if value is greater that maximum, assign to max and second max
    if (val > max) {
      secondMax = max;
      max = val;
    } else if (val > secondMax) {
    // assign only second max if value is greater than second max
      secondMax = val;
    }
  }
  return secondMax;
}

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(findSecondMax(args));
}
