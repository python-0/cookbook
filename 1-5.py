#get item by priority.
import heapq

class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self,item,priority):
		heapq.heappush(self._queue, (-priority,self._index,item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]


p = PriorityQueue()
p.push('a',1)
p.push('b',20)
p.push('c',3)
p.push('d',2)

#print :b c d a
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())