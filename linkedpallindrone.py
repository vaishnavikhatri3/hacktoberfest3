# Python3 program to check if a 
# linked list with loop is palindrome 
# or not.

# Node class 
class Node: 

	# Constructor to initialize the 
	# node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to find loop starting node. 
# loop_node -. Pointer to one of 
# the loop nodes head -. Pointer to 
# the start node of the linked list
def getLoopstart(loop_node,head): 

	ptr1 = loop_node 
	ptr2 = loop_node 

	# Count the number of nodes in 
	# loop 
	k = 1
	i = 0
	while (ptr1.next != ptr2):	 
		ptr1 = ptr1.next
		k = k + 1

	# Fix one pointer to head 
	ptr1 = head 

	# And the other pointer to k 
	# nodes after head 
	ptr2 = head
	i = 0
	while (i < k):
		ptr2 = ptr2.next
		i = i + 1

	# Move both pointers at the same pace, 
	# they will meet at loop starting node 
	while (ptr2 != ptr1):	 
		ptr1 = ptr1.next
		ptr2 = ptr2.next
	
	return ptr1 

# This function detects and find 
# loop starting node in the list
def detectAndgetLoopstarting(head): 
	slow_p = head
	fast_p = head
	loop_start = None

	# Start traversing list and detect loop 
	while (slow_p != None and fast_p != None and
		fast_p.next != None): 
		slow_p = slow_p.next
		fast_p = fast_p.next.next

		# If slow_p and fast_p meet then find 
		# the loop starting node
		if (slow_p == fast_p):	 
			loop_start = getLoopstart(slow_p, 
									head) 
			break
		
	# Return starting node of loop 
	return loop_start 

# Utility function to check if 
# a linked list with loop is 
# palindrome with given starting point. 
def isPalindromeUtil(head, loop_start): 
	ptr = head 
	s = [] 

	# Traverse linked list until last node 
	# is equal to loop_start and store the 
	# elements till start in a stack 
	count = 0
	while (ptr != loop_start or count != 1):	 
		s.append(ptr.data) 
		if (ptr == loop_start) :
			count = 1
		ptr = ptr.next
	
	ptr = head 
	count = 0

	# Traverse linked list until last node is 
	# equal to loop_start second time 
	while (ptr != loop_start or count != 1):	 
		# Compare data of node with the top of stack 
		# If equal then continue 
		if (ptr.data == s[-1]): 
			s.pop() 

		# Else return False 
		else:
			return False

		if (ptr == loop_start) :
			count = 1
		ptr = ptr.next
	
	# Return True if linked list is 
	# palindrome 
	return True

# Function to find if linked list
# is palindrome or not 
def isPalindrome(head):

	# Find the loop starting node 
	loop_start =
	detectAndgetLoopstarting(head) 

	# Check if linked list is palindrome 
	return isPalindromeUtil(head, 
							loop_start) 

def newNode(key):
	temp = Node(0) 
	temp.data = key 
	temp.next = None
	return temp 

# Driver code
head = newNode(50) 
head.next = newNode(20) 
head.next.next = newNode(15) 
head.next.next.next = newNode(20) 
head.next.next.next.next = newNode(50) 

# Create a loop for testing 
head.next.next.next.next.next =
head.next.next

if(isPalindrome(head) == True):
	print("Palindrome")
else:
	print("Not Palindrome") 
# This code is contributed by Arnab Kundu
