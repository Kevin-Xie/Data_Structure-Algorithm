
from LinkList import LinkList, ListNode


list1 = LinkList()

list1.append(ListNode(1))
list1.append(ListNode(2))
list1.append(ListNode(3))
list1.append(ListNode(3))
list1.append(ListNode(4))
list1.append(ListNode(4))
list1.append(ListNode(5))
list1.append(ListNode(6))
list1.append(ListNode(7))
list1.append(ListNode(7))
list1.append(ListNode(8))
list1.append(ListNode(9))
list1.append(ListNode(9))
list1.append(ListNode(9))


def removeDuplicate(head):
	lastVal = None
	current = head.next
	while current:
		nextNode = current.next
		if current.val == lastVal:
			current.next = nextNode.next
		else:
			lastVal = current.val
		current = nextNode
	return head



if __name__ == '__main__':
		main()	