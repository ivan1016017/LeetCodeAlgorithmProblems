function areSentencesSimilar(sentence1: string[], sentence2: string[], similarPairs: string[][]): boolean {
    if(sentence1.length !== sentence2.length) return false;
    
    let map: any = new Map<string, Set<string>>();
    for(const [key, value] of similarPairs){
    if(!map.has(key))
        map.set(key, new Set<string>());
    if(!map.has(value))
        map.set(value, new Set<string>());
    map.get(key).add(value);
    map.get(value).add(key);
    }

    for(let i = 0 ; i < sentence1.length ; i++)
    {
    let word1 = sentence1[i];
    let word2 = sentence2[i];
    if(word1 === word2) continue;
    if(!map.get(word1)?.has(word2))
        return false;
    if(!map.get(word2)?.has(word1))
        return false;
    }
    return true;

};