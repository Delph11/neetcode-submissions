class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Find the length of each array
        n = len(nums1)
        m = len(nums2)
        # Find the total if it is odd or even to assign the case
        if (n+m)%2 == 0:
            flag = 0
        else:
            flag = 1
        # Now we have to assign the smaller one to A and the larger one to B
        if n<=m:
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        # Now we have to start the BS to find the cut
        # REMOVED: the special if len(A)==0 block with float('-inf') as lo/hi.
        # For an empty A this gives lo,hi = 0,-1, which is fine now (see while True below)
        lo, hi = 0, len(A)-1
        half = (len(A)+len(B))//2

        while True:  # CHANGED: was "while lo<=hi", which could never reach mid = -1 (A gives 0 elements)
            # REMOVED: the if len(A)==0 branch inside the loop
            mid = (lo+hi)//2   # can become -1, meaning A gives 0 elements
            Bmid = (half-(mid+1))-1  # Eg. if mid is 3, A gives 4 elements, so B gives 6-4 = 2 elements, so B's last left index is 1

            # CHANGED: guarded reads, so an edge cut never reads out of range or wraps around
            Aleft  = A[mid]      if mid >= 0            else float('-inf')  # rightmost element of A's left partition
            Aright = A[mid+1]    if (mid+1) < len(A)    else float('inf')   # leftmost element of A's right partition
            Bleft  = B[Bmid]     if Bmid >= 0           else float('-inf')
            Bright = B[Bmid+1]   if (Bmid+1) < len(B)   else float('inf')

            # Now we will do the cross comparison
            if Aleft>Bright:    # too many elements from A
                hi = mid-1
            elif Bleft>Aright:  # too few elements from A
                lo = mid+1
            else:
                # CHANGED: return only here, when the cut is valid
                if flag == 0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)