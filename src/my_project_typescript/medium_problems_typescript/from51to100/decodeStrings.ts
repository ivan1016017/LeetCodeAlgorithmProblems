function decodeString(s: string): string {
    let stack: string[] = [];

    for(let c of s){
        if(c === ']'){
            let char:any = stack.pop();
            let no = ''
            let curr: string = '';
            while(isNaN(Number(char))){
                curr = char + curr;
                char = stack.pop();
            }
            while(!isNaN(Number(char))){
                no = char + no;
                char = stack.pop();
            }
            curr = curr.repeat(Number(no));
            stack.push(char);
            stack.push(curr);
        }
        else{
            stack.push(c);
        }
    }

    return stack.join('').split("[").join('');
};