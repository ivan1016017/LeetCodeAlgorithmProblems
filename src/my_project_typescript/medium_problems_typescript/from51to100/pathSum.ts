
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
 

 function pathSum(root: TreeNode | null, targetSum: number): number[][] {

    if (!root){
        return []
    }
    if (root.left === null && root.right === null){
        if (targetSum === root.val){
            return [[root.val]]
        }
        else {
            return []
        }
    }

    let a: Array<Array<number>> = pathSum(root.left, targetSum - root.val).concat(pathSum(root.right, targetSum-root.val))

    let temp: Array<Array<number>> = []

    for (let i of a){
        temp.push([root.val].concat(i))
    }
    return temp
};