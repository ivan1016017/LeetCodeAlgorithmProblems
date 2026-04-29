// Definition for a Node.
export class _Node {
    val: number;
    next: _Node | null;
    random: _Node | null;

    constructor(val?: number, next?: _Node | null, random?: _Node | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
        this.random = random ?? null;
    }
}