function isMatch(s: string, p: string): boolean {

    if (!p){
        return !s;
    } 
    if (!s) {
        return (p.length > 1 && p[1] === '*' && isMatch(s, p.slice(2,p.length)))
    }
    let Matched: boolean = (p[0] === '.' || p[0] === s[0])
    if (p.length > 1 && p[1] === '*'){
        return (Matched && isMatch(s.slice(1,s.length), p)) || isMatch(s, p.slice(2,p.length))
    }
        
    return Matched && isMatch(s.slice(1,s.length), p.slice(1,p.length))
};