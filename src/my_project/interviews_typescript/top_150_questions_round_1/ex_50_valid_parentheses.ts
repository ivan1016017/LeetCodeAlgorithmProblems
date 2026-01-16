function isValid(s: string): boolean {

    const dicParentheses: {[key: string]: string} = {
        '(': ')',
        '[': ']',
        '{': '}'        
    }

    const checkList: string[] = []

    for (const p of s){
        if (p in dicParentheses){
            checkList.push(p)
        }else{
            if (checkList.length === 0 || 
                dicParentheses[checkList.pop()!] !== p){
                return false 
            }
        }
    }

    return checkList.length === 0
    
};        
