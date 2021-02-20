import collections

nums = [1,2,2,3]
cnt = collections.Counter(nums)

print(cnt,max(cnt,key = cnt.get),cnt.get(3))

