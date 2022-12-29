function largestVariance(s: string): number {

    let res: number = 0
    let chars: string[] = []

    for (let letter of s){
        if (!chars.includes(s)){
            chars.push(letter)
        }
    }

    for (let i = 0; i < chars.length; i++){
        for (let j = i+1; j < chars.length; j++ ){
            let c1:string = chars[i]
            let c2:string = chars[j]
            let diff: number = 0
            let min_diff: number = 0
            let max_diff: number = 0
            let last_c1_diff:number = 0
            let last_c2_diff: number = 0
            let meet_c1:boolean = false 
            let meet_c2:boolean = false 

            for (let c of s){
                if (c===c1){
                    meet_c1 = true 
                    diff+=1
                    max_diff = Math.max(last_c1_diff,max_diff)
                    last_c1_diff = diff 
                }
                else if (c===c2){
                    meet_c2 = true 
                    diff-=1
                    min_diff = Math.min(last_c2_diff,min_diff)
                    last_c2_diff = diff 
                }
                else{
                    continue
                }
                if (meet_c1 && meet_c2){
                    res = Math.max(diff-min_diff,max_diff-diff,res)
                }
            }

        }
    }

    return res 



};



function largestVarianceTwo(s: string): number {
    const freqObj: Record<string, number> = {};
    
    for (let i = 0; i < s.length; i++) {
        const currStr = s.charAt(i);
        
        if (freqObj[currStr]) {
            freqObj[currStr]++
        } else {
            freqObj[currStr] = 1;
        }
    }
    
    const freqObjKeys = Object.keys(freqObj);
    
    let variance: number = 0;
    
    for (let primaryString of freqObjKeys) {
        
        for (let secondaryString of freqObjKeys) {
            
            if (primaryString === secondaryString) continue;
            
            let primaryFreq: number = 0;
            let secondaryFreq: number = 0;
            let secondaryCharCount: number = freqObj[secondaryString];
            
            for (let i = 0; i < s.length; i++) {
                const currentStr: string = s[i];
                
                if (currentStr === primaryString) primaryFreq++;
                if (currentStr === secondaryString) {
                    secondaryFreq++;
                    secondaryCharCount--
                }
                
                if ((primaryFreq > 0 && secondaryFreq > 0) && (primaryFreq > secondaryFreq)) {
                    variance = Math.max(variance, (primaryFreq - secondaryFreq))
                }
                
                if (primaryFreq < secondaryFreq && secondaryCharCount > 0) {
                   primaryFreq = 0;
                   secondaryFreq= 0;
                }
            } 
            
        }
    }
    
    return variance;
};