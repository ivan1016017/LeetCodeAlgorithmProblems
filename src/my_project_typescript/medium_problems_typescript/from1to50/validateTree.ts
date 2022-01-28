
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
 

 function isValidBST(root: TreeNode | null): boolean {


    function helper(node: TreeNode | null, minv: number = -(2**32), maxv: number = 2**32 ):boolean{
        if (node===null){
            return true
        }

        if (!(node.val > minv && node.val < maxv)){

            return false 
        }

        let b1: boolean = helper(node.left, minv, node.val)


        let b2: boolean = helper(node.right, node.val, maxv)

        return b1 && b2
    }

    return helper(root)
    

};



let sampleTreeOne: TreeNode = new TreeNode(8, new TreeNode(-70),new TreeNode(81))


console.log(isValidBST(sampleTreeOne))