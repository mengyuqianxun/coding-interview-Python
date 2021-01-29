class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m,n = len(heights),len(heights[0])
        ans = 0
        left,right = 0,10**6-1

        while left <= right:
        	mid = (left + right)//2
        	q = collections.deque([(0,0)])
        	set_h = {(0,0)}

        	while q:
        		x,y = q.popleft()
        		for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        			if 0 <= nx < m and 0 <= ny <n and \
        			(nx,ny) not in set_h and \
        			abs(heights[nx][ny]-heights[x][y]) <= mid:
        				q.append((nx,ny))
        				set_h.add((nx,ny))
        	if (m-1,n-1) in set_h:
        		ans = mid
        		right = mid - 1
        	else:
        			left = mid + 1
        return ans



