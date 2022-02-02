

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
 


function zigzagLevelOrder(root: TreeNode | null): number[][] {
    if (!root) return [];
    let stack: TreeNode[] = [root];
    const res: number[][] = [];
    let i = 0;
  
    while (stack.length) {
      const newStack: TreeNode[] = [];
      res.push([]);
  
      for (const node of stack) {
        res[i].push(node.val);
        if (node.left) newStack.push(node.left);
        if (node.right) newStack.push(node.right);
      }
  
      stack = newStack;
      i++;
    }
  
    for (let i = 1; i < res.length; i += 2) res[i].reverse();
    return res;
  }