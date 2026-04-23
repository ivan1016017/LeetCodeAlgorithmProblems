function longestPalindrome(s: string): string {
    let start = 0, maxLen = 1;

    const expand = (left: number, right: number): void => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        const length = right - left - 1;
        if (length > maxLen) {
            maxLen = length;
            start = left + 1;
        }
    };

    for (let i = 0; i < s.length; i++) {
        expand(i, i);       // odd-length
        expand(i, i + 1);   // even-length
    }

    return s.substring(start, start + maxLen);
}
