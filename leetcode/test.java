class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    // i'd make this private
    private int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        if(root==null)
            return 0;

        dfs(root);
        return max;
    }

    private int dfs(TreeNode node){
        // you don't have a base case

        // at a glance, this looks messy
        // there is not proper spacing in your code
        int leftSum = (node.left == null) ? 0 : dfs(node.left);
        int rightSum = (node.right == null) ? 0 : dfs(node.right);
        int sum = leftSum + rightSum + node.val;
        int maxBranch = node.val + Math.max(leftSum, rightSum);
        int nodeMax = Math.max(node.val, Math.max(sum, maxBranch)); //Maximum path through this node
        max = Math.max(max, nodeMax);
        return Math.max(node.val, maxBranch); // Return maximum path to ancestor via any one branch
    }
}