'''
Tree Job Application Applier

You've found yourself in the role of a job applicant. You have a list of recruiters at a large company you need to contact. After some preliminary analysis, being the adept applicant you are, you figure out that the recruiter information is stored in the form of a Binary tree! Besides the root, each recruiter has one and only one parent node. All directly linked recruiters keep tabs on each other and they will automatically discard your application if you apply to both of them. Each recruiter also has an associated number of positions (node value) that they can send your application to (Assume all recruiters have a unique list of positions).

Determine the maximum positions you can get your application sent to, without having your application discarded.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum number of applications = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum number of applications = 4 + 5 = 9.
'''



def find_applications(root):
    memo = {}
    def find_rec(node, is_contactable):
        key = (id(node), is_contactable)

        if not node:
            return 0

        if key in memo:
            return memo[key]

        no_contact_left = find_rec(node.left, False)
        no_contact_right = find_rec(node.right, False)

        if is_contactable:
            memo[key] = node.val + no_contact_left + no_contact_right
        else:
            contact_left = find_rec(node.left, True)
            contact_right = find_rec(node.right, True)
            memo[key] = max(contact_left, no_contact_left) + max(contact_right, no_contact_right)

        return memo[key]



    return max(find_rec(root, True), find_rec(root, False))
