#^^^^^^^^^^^^^^COPY^^^^^^^^^^^^^^^
# Python program to do Morris inOrder Traversal:
# inorder traversal without recursion and without stack
# https://www.geeksforgeeks.org/morris-traversal-for-preorder/

#TC=N,SC=1

class Node:
	"""A binary tree node"""

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def morris_traversal(root):
	"""Generator function for
	iterative inorder tree traversal"""

	current = root

	while current:

		if current.left is None:
			yield current.val
			current = current.right
		else:

			# MAKE THREAD BY MOVING TOWARDS RIGHT THEN YIELD VALUES FROM LEFT 
			pre = current.left
			while pre.right and pre.right is not current: #Find rightmost node in current left subtree OR node whose right child == current
				pre = pre.right                            #pre.right child must be present and no thread is created till now

			if pre.right is None: # no thread is created till now

				# Make current as right
				# child of its inorder predecessor
				pre.right = current #creating the thread
                yield current.val
				current = current.left  #now current is actually moved towards left 

			else:
				# Revert the changes made
				# in the 'if' part to restore the
				# original tree. i.e., fix
				# the right child of predecessor
				pre.right = None #since pre is pointing at the leaf node i.e. 6 in copy example
				# yield current.val    ######
				current = current.right


# Driver code
"""
Constructed binary tree is
			1
		/ \
		2	 3
	/ \
	4	 5
"""
root = Node(1,
			right=Node(3),
			left=Node(2,
					left=Node(4),
					right=Node(5)
					)
			)

for v in morris_traversal(root):
	print(v, end=' ')

