
//  * Definition for a binary tree node.
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


 function binaryTreePaths(root: TreeNode | null): string[] {

    if (root  === null){
        return []
    }

    function traversal(node: TreeNode, path: Array<string>){
        if (node.left === null && node.right === null) {
            answer.push(path.join("->"))
        }

        if (node.left){
            path.push(node.left.val.toString())
            traversal(node.left, path)
            path.pop()
        }
        if (node.right){
            path.push(node.right.val.toString())
            traversal(node.right, path)
            path.pop()
        }
    }


    let answer: Array<string> = []
    let path = [root.val.toString()]
    traversal(root, path)

    return answer

};





