### To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival