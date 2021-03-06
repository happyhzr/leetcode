class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


if __name__ == '__main__':
    s = Solution()

    num1 = [1, 2, 3, 0, 0, 0]
    m = 3
    num2 = [2, 5, 6]
    n = 3
    s.merge(num1, m, num2, n)
    print(num1)
