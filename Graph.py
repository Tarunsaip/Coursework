from collections import defaultdict

from State import TERMINAL_STATE

import time


class Graph:

	def __init__(self):

		self.bfs_parent = {}
		self.dfs_parent = {}

		self.expandedBFS = 0
		self.expandedDFS = 0

	def BFS(self, s):
		self.expandedBFS = 0
		self.bfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}
		s.level = 0

		queue = [s]
		while queue:
			self.expandedBFS += 1

			u = queue.pop(0)

			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				queue.clear()
				self.bfs_parent[TERMINAL_STATE] = u
				return self.bfs_parent

			for v in reversed(u.successors()):
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					self.bfs_parent[v] = u
					v.level = u.level + 1
					queue.append(v)
					visited[(v.missionaries, v.cannibals, v.dir)] = True

		return {}

	def DFS(self, s):
		self.expandedDFS = 0
		self.dfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}

		stack = [s]
		while stack:
			u = stack.pop()
			self.expandedDFS += 1

			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.expandedDFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				self.dfs_parent[TERMINAL_STATE] = u
				stack.clear()
				return self.dfs_parent

			for v in u.successors():
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					visited[(v.missionaries, v.cannibals, v.dir)] = True
					self.dfs_parent[v] = u
					stack.append(v)
		return {}

	def printPath(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None: 
			return
		if tail == TERMINAL_STATE: tail = parentList[tail]

		stack = []

		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]

		while stack:
			print(stack.pop())
