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


public class MaxPathSumObjectOrientedShim {
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

    public static int maxPath = 0;

    private static int maxPathSumRec(Node node) {
        if (node == null) {
            return 0;
        }

        int maxLeft = maxPathSum(node.left);
        int maxRight = maxPathSum(node.right);

        int maxBranch = Collections.max(List.of(
            maxLeft + node.val,
            maxRight + node.val,
            node.val
        ));

        maxPath = Collections.max(List.of(
            maxLeft + node.val + maxRight,
            maxBranch,
            maxPath
        ));

        return maxBranch;
    }

    public static int maxPathSum(Node root) {
        maxPath = 0;

        maxPathSumRec(root);
        return maxPath;
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
