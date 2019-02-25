import copy


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkList():
    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def setLength(self, length):
        self.length = length

    def add(self, data):
        datanode = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = datanode
        self.length += 1

    def printLink(self):
        node = self.head.next
        pstr = ''
        while node:
            pstr += str(node.data) + ' '
            node = node.next
        print(pstr[0:-1])

    def getLength(self):
        return self.length

    def getNodeByIndex(self, index):
        node = self.head
        i = 0
        if index >= self.length or index < 0:
            raise IndexError
        while i < index:
            node = node.next
            i += 1
        return node

    def delete(self, index):
        if index > self.length or index <= 0:
            raise IndexError
        elif index == self.length:
            node = self.getNodeByIndex(index - 1)
            node.next = None
        else:
            preNode = self.getNodeByIndex(index - 1)
            nextNode = self.getNodeByIndex(index + 1)
            preNode.next = nextNode

    def getMiddleNode(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def isPlaindrome(self, comlinkList):
        comHead = comlinkList.getHead()
        cur = self.head.next
        com = comHead.next
        while cur:
            if cur.data == com.data:
                cur = cur.next
                com = com.next
            else:
                return False
        return True

    def reverseSelfLink(self):
        pre = None
        cur = self.head.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.head.next = pre

    @staticmethod
    def reverseLink(head):
        pre = None
        cur = head.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head.next = pre
        return head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        pre = head
        cur = head.next
        while cur:
            t = cur
            count = 1
            while count < k and t:
                t = t.next
                count += 1
            if count == k and t:
                for _ in range(k - 1):
                    lat = cur.next
                    cur.next = lat.next
                    lat.next = pre.next
                    pre.next = lat
                pre = cur
                cur = pre.next
            else:
                break

        return head


if __name__ == '__main__':
    # print('')
    while True:
        try:
            linkList = LinkList()
            listStr = [str(x) for x in input().split(" ")]
            # print(listStr)
            length = int(listStr[0])
            K = int(listStr[-1])
            for i in range(1, length + 1):
                linkList.add(listStr[i])
            # linkList.printLink()
            head = linkList.getHead()
            linkList.reverseKGroup(head, K)
            linkList.printLink()
        except EOFError:
            break
