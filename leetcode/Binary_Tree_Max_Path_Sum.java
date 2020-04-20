package leetcode;

public class Binary_Tree_Max_Path_Sum {
    int highest_sum;

    class Node {
        Node left = null;
        Node right = null;
        int val;

        Node(int val) {
            this.val = val;
        }
    }

    private int dfs(Node node) {
        if(node == null)
            return 0;

        int left = dfs(node.left);
        int right = dfs(node.right);
        int best_child = Math.max(left, right);

        int sum_with_best_child = node.val + best_child;

        int sum_with_both_children = node.val + left + right;

        this.highest_sum = Math.max(sum_with_both_children, this.highest_sum);

        if(sum_with_best_child < 0)
            return 0;
        return sum_with_best_child;
    }

    public int maxPathSum(Node root) {
        this.highest_sum = Integer.MIN_VALUE;

        dfs(root);
        return this.highest_sum;
    }
}


Binary_Tree_Max_Path_Sum sol = new Binary_Tree_Max_Path_Sum();
sol.maxPathSum(new Node(3));

// # root = Node(-10)
// # root.left = Node(9)
// # root.right = Node(20)
// # root.right.left = Node(15)
// # root.right.right = Node(7)

// root = Node(5)
// root.left = Node(4)
// root.right = Node(8)
// root.left.left = Node(11)
// root.right.left = Node(13)
// root.right.right = Node(4)
// root.right.left.left = Node(7)
// root.right.left.right = Node(2)
// root.right.right.right = Node(1)

// # [5,4,8,11,null,13,4,7,2,null,null,null,1]

// print(sol.maxPathSum(root))
