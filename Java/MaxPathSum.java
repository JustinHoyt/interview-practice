import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Map.Entry;
import java.util.function.Function;

import org.junit.Test;


public class MaxPathSum {
    class Node {
        public int val;
        public Node left;
        public Node right;

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static int maxPathSum(Node root) {
        var closure = new Object() {
            Function<Node, Integer> maxPathSum;
            int maxPath = root != null ? root.val : 0;
        };

        closure.maxPathSum = node -> {
            if (node == null) {
                return 0;
            }

            int maxLeft = closure.maxPathSum.apply(node.left);
            int maxRight = closure.maxPathSum.apply(node.right);

            int maxBranch = Collections.max(List.of(
                maxLeft + node.val,
                maxRight + node.val,
                node.val
            ));

            closure.maxPath = Collections.max(List.of(
                maxLeft + node.val + maxRight,
                maxBranch,
                closure.maxPath
            ));

            return maxBranch;
        };

        closure.maxPathSum.apply(root);
        return closure.maxPath;
    }

    @Test
    public void testMaxPathSum() {
        assertEquals(42, maxPathSum(
            new Node(-10,
                new Node(9),
                new Node(20,
                    new Node(15),
                    new Node(7)
                )
            )
        ));
    }
}
