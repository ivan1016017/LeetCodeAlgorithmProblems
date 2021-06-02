function isValid(s: string): boolean {
    let result: boolean = true;
    let temp: string = "";
    let candidates: string[] = ["(", "[", "{"];
    let tempObject: any = {")": "(", "]": "[", "}": "{"};

    for (let item of s) {
        if (candidates.includes(item)){
            temp += item;
        }
        if (!candidates.includes(item)){
            if (item === ")"){
                if (temp[temp.length-1] !== tempObject[item]){
                    return false;
                } 
                if (temp[temp.length-1] === tempObject[item]){
                    temp = temp.slice(0, temp.length -1);
                } 
            }
            if (item === "]"){
                if (temp[temp.length-1] !== tempObject[item]){
                    return false;
                } 
                if (temp[temp.length-1] === tempObject[item]){
                    temp = temp.slice(0, temp.length -1);
                } 
            }
            if (item === "}"){
                if (temp[temp.length-1] !== tempObject[item]){
                    return false;
                } 
                if (temp[temp.length-1] === tempObject[item]){
                    temp = temp.slice(0, temp.length -1);
                } 
            }
        }
    }
    if (temp.length === 0 ){
        return true;
    } else {
        return false;
    }
};

console.log(isValid("()"));
console.log(isValid("()[]{}"));
console.log(isValid("([)]"));