#-*-coding:utf-8 -*-

class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, val=None, next=None):
		super(ListNode, self).__init__()
		self.val = val
		self.next = next
		

class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):
		super(LinkList, self).__init__()
		self.head = ListNode(val='head', next=None)

	def all(self):
		pointer = self.head
		while pointer is not None:
			print pointer.val
			pointer = pointer.next

	def append(self, newNode):
		pointer = self.head
		while pointer.next is not None:
			pointer = pointer.next
		pointer.next = newNode			

	# 翻转链表
	def reverse(self):
		current = self.head
		last = None
		while current is not None:
			nextNode = current.next
			current.next = last
			last = current
			current = nextNode
		self.head = last	
		return self
	
	# 逆序打印链表		
	def reversePrint(self):
		pointer = self.head
		result = []
		while pointer is not None:
			result.insert(0, pointer.val)
			pointer = pointer.next
		return result



l = LinkList()
l.append(ListNode(1))
l.append(ListNode(2))
l.append(ListNode(3))
l.append(ListNode(4))
l.append(ListNode(5))
l.all()

print l.reversePrint()
l.reverse().all()