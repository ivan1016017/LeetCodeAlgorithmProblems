
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


function widthOfBinaryTree(root: TreeNode | null): number {

    let maxWidth = 0;
    if (!root) return maxWidth;
    const queue: [TreeNode, number][] = [[root, 0]]; // TreeNode, Position
    while (queue.length) {
      const levelWidth = queue[queue.length - 1][1] - queue[0][1] + 1;
      maxWidth = Math.max(maxWidth, levelWidth);
      const len = queue.length;
      for (let i = 0; i < len; i++) {
        const [node, pos] = queue.shift()!;
        if (node.left) {
          queue.push([node.left, pos * 2]);
        }
        if (node.right) {
          queue.push([node.right, pos * 2 + 1]);
        }
      }
    }
    return maxWidth;

};