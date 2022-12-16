function isValid(s: string): boolean {

    let temp: string[] = []
    let validParentheses: string[] = ['(','[','{']

    for (let p of s){
        if (validParentheses.includes(p)){
            temp.push(p)
        }
        else{
            if (!temp){
                return false 
            }
            let other_half = temp.pop()
            if (p == ')'){
                if (other_half != '('){
                    return false;
                }
            }
            else if (p == ']'){
                if (other_half != '['){
                    return false 
                }
            }
            else if (p == '}'){
                if (other_half != '{'){
                    return false 
                }
            }
            else{
                return false 
            }

        }
    }


    if (temp.length>0){
        return false 
    }

    return true 

};

console.log(isValid('()'))