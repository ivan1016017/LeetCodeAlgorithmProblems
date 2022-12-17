function helper(s: string,l:number,r:number): string {
    while (l>=0 && r<s.length && s[l]==s[r]){
        l-=1;r+=1
        
    }
    return s.slice(l+1,r)
};

function longestPalindrome(s: string): string {

    let answer:string = ''
    let temp:string

    for (let i = 0; i < s.length; i++){

        temp = helper(s,i,i)
        
        if (temp.length> answer.length){
            answer = temp 
        }    
        temp = helper(s,i,i+1)
        if (temp.length > answer.length){
            answer = temp 
        }
    }
    return answer 
};

