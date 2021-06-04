function strStr(haystack: string, needle: string): number {
  let needleLenght: number = needle.length;
  let flag: boolean;
  let index: number = -1;
  if (needleLenght === 0) {
    return 0;
  } else if (haystack.length === 0 && needleLenght !== 0) {
    return -1;
  } else {
    for (let i = 0; i < haystack.length; i++) {
      flag = true;
      if (
        haystack[i] === needle[0] &&
        haystack.slice(i).length >= needleLenght
      ) {

        index = i;
        for (let j = 0; j < needleLenght; j++) {
   
          if (needle[j] !== haystack[i + j]) {
            index = -1;
            flag = false;
            break;
          }

        }
        if (flag) {
            return index;
          }
      }
    }
    return index;
  }
}

// console.log(strStr("hello", "ll"));
// console.log(strStr("aaaaa", "bba"));
strStr("mississippi","issip");
