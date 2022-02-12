function wordBreak(s: string, wordDict: string[]): boolean {
    if(s.length < 1) return false; 
    const dp: boolean[] = new Array(s.length + 1).fill(false);
    dp[0] = true; 
    
    for(let i = 0; i < s.length; i++) {
        if(dp[s.length]) return dp[s.length]; 
        if(dp[i]) {
         for(let word of wordDict) {
            if(word === s.slice(i, i + word.length)) {
               dp[i + word.length] = true; 
            }
        }     
      }
    }

    return dp[s.length]
    
};