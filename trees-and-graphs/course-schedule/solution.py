class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # keep track of what courses a course is a prereq for and its indegree
        indegrees = [0] * numCourses
        prereqs = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            prereqs[pair[1]].append(pair[0])
            indegrees[pair[0]] += 1
        
        # put all courses with indegree = 0 in queue
        q = deque([])
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
        
        # after popping from queue, decrement indegrees of prereqs 
        # add prereq to queue if indegree goes to 0
        while q:
            print(q)
            course = q.popleft()
            for prereq in prereqs[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)
        
        # if there are still elements with indegree > 0, return false
        if sum(indegrees) > 0:
            return False
        return True