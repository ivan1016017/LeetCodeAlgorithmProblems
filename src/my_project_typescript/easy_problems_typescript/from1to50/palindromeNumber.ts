function isPalindrome(x: number): boolean {
  let tempString: string = x.toString();
  let lengthString = tempString.length;
  let result: boolean = true;
  if (x < 0) {
    result = false;
    return result;
  } else {
    for (let i = 0; i < tempString.length; i++) {
      if (tempString[i] !== tempString[lengthString-1 - i]) {
        result = false;
        return result;
      }
    }
    return result;
  }
}

console.log(isPalindrome(-102));
console.log(isPalindrome(1008001));
