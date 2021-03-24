class Solution(object):
	def findMedianSortedArrays_NlogN(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		mlist = nums1 + nums2
		mlist.sort()
		l = len(mlist)

		
		if l%2 == 0 :
			return (mlist[l//2-1] + mlist[l//2])/2
		else :
			return mlist[l//2]

	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		# for 문 한번만 돌면서 /2 해야 logN 만족 

		l = len(nums1) + len(nums2)
		# 길이 합이 홀수 일 때
		if l%2 == 1 :
			return self.findKth(nums1,nums2,l//2)
		# 짝수 일 때, 중간의 좌우 인덱스 찾기 
		else : 
			return (self.findKth(nums1,nums2,(l//2)-1) + self.findKth(nums1,nums2,(l//2))/2)
	
	def findKth(self, a,b,k) :
		# a가 항상 작게
		if len(a)>len(b) :
			a,b = b,a
		# a가 없을 때 
		if not a : 
			return b[k]

		# 종료 조건
		# pass

		i = len(a)//2
		j = k - i

		if a[i] > b[j] : 
			return self.findKth(a[:i], b[j:], i)
		else :
			return self.findKth(a[i:], b[:j], j)


l1 = [1,2,3,4]
l2 = [2,4,6,8]
# 1 2 2 3 4 4 6 8 -> 3,4 에서 답 3.5
print(Solution().findMedianSortedArrays(l1, l2))