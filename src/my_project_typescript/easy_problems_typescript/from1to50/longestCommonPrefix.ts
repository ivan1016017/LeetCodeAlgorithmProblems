function longestCommonPrefix(strs: string[]): string {
    let result: string = "";

    if (strs.length === 0){
        return result;
    }
    let count: number = 0;
    for (let letter of strs[0]){
        for (let item of strs){
            if (!item.slice(count, count+ 1).includes(letter)){
                return result;
            }
        }
        result += letter;
        count += 1;
    }
    return result;
};

console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix(["dog"]));
console.log(longestCommonPrefix(["aa","ab"]));
console.log(longestCommonPrefix(["c","acc","ccc"]));


