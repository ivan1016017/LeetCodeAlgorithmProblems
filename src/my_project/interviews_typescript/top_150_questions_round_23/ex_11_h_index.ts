function hIndex(citations: number[]): number {
    citations.sort((a, b) => b - a);
    const lenCit: number = citations.length;
    let answer: number = 0;

    for (let i = 0; i < lenCit; i++) {
        if (citations[i] >= i + 1) {
            answer = i + 1;
        }
    }

    return answer;
};        
