class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break

                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        def backtrack(i, add):
            if i >= len(candidates) or add >= target:
                if add == target:
                    ans.append(tmp)
                return
            tmp.append(candidates[i])
            backtrack(i, add + candidates[i]) 
            tmp.pop()
            backtrack(i + 1, add)
        backtrack(0, 0)
        return ans 