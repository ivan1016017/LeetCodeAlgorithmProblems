function reverse(x: number): number {
    let solution: string = "";
  let sign = 0;
  if (x < 0) {
    sign = -1;
  } else {
    sign = 1;
  }
  let temp: string = x.toString();
  for ( let i = 0; i < temp.length; i++){
    solution = temp[i] + solution;
  }
  if (sign === 1){
      return parseInt(solution);
  } else {
    return -parseInt(solution);
  }

}

console.log(reverse(1234));
console.log(reverse(-1234));

