function maxPoints(points: number[][]): number {
    const n = points.length;
    if (n <= 2) return n;
    let result = 2;
    for (let i = 0; i < n; i++) {
        const slopes = new Map<string, number>();
        for (let j = i + 1; j < n; j++) {
            let dx = points[j][0] - points[i][0];
            let dy = points[j][1] - points[i][1];
            const g = gcd(Math.abs(dx), Math.abs(dy));
            dx /= g;
            dy /= g;
            if (dx < 0) {
                dx = -dx;
                dy = -dy;
            } else if (dx === 0) {
                dy = Math.abs(dy);
            }
            const key = `${dx},${dy}`;
            slopes.set(key, (slopes.get(key) || 0) + 1);
        }
        if (slopes.size > 0) {
            for (const count of slopes.values()) {
                result = Math.max(result, count + 1);
            }
        }
    }
    return result;
}

function gcd(a: number, b: number): number {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

console.log(maxPoints([[1, 1], [2, 2], [3, 3]]));
console.log(maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]));
