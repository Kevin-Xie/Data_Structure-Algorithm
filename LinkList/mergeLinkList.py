#-*-coding:utf-8 -*-

# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

from LinkList import LinkList, ListNode


list1 = LinkList()
list2 = LinkList()

list1.append(ListNode(1))
list1.append(ListNode(3))
list1.append(ListNode(5))
list1.append(ListNode(7))
list1.append(ListNode(9))

list2.append(ListNode(2))
list2.append(ListNode(4))
list2.append(ListNode(6))
list2.append(ListNode(8))
list2.append(ListNode(10))



def mergeLinkList(list1, list2):
	head = list1.head
	current = head
	current1 = list1.head.next
	current2 = list2.head.next
	while current1 and current2:
		if current1.val < current2.val:
			current.next = current1
			current1 = current1.next
		else:
			current.next = current2
			current2 = current2.next
		current = current.next
	if current1:
		current.next = current1
	if current2:
		current.next = current2
	return head	
				


def main():
	head = mergeLinkList(list1, list2)
	while head:
		print head.val
		head = head.next

if __name__ == '__main__':
	main()