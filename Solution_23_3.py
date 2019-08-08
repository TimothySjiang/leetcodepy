class Solution(object):
    def mergeKLists(self, lists):
        h = []
        for i, n in enumerate(lists):
            if n:
                heapq.heappush(h, (n.val, i, n))

        r = t = ListNode(0)

        while h:
            i, n = heapq.heappop(h)[1:]
            t.next = n
            t = t.next
            n = n.next
            if n:
                heapq.heappush(h, (n.val, i, n))

        return r.next