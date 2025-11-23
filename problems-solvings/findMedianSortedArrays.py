class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
      #  mergeArr = sorted(nums1.extend(nums2));
        # nums1.extend(nums2) to add list to anothe list
       # nums1.append(2) to add item to the list
        mergeArr = sorted([*nums1, *nums2]);
        arrLen = len(mergeArr)
        middeIndex = arrLen //2
        if arrLen % 2 == 0:
            # Case 1: Even length (e.g., Length 4, middeIndex = 2)
            # The two middle elements are at index (2 - 1) = 1 and index 2.
            # Use middeIndex and middeIndex - 1.
            return (mergeArr[middeIndex]+mergeArr[middeIndex-1])/2
        else :
            return mergeArr[middeIndex]
        