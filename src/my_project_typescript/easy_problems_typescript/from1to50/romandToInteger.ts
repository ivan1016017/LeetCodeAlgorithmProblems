function romanToInt(s: string): number {
  // initialize variables
  let lenString: number = s.length;
  let result: number;
  let tempObj: any = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };

  // initialize result

  result = tempObj[s[lenString - 1]];

  for (let i = 1; i < lenString; i++) {
    if (tempObj[s[lenString - i]] > tempObj[s[lenString - 1 - i]]) {
      result = result - tempObj[s[lenString - 1 - i]];
    } else {
      result = result + tempObj[s[lenString - 1 - i]];
    }
  }
  return result;
}

console.log(romanToInt("IV"));
console.log(romanToInt("III"));
console.log(romanToInt("LVIII"));
