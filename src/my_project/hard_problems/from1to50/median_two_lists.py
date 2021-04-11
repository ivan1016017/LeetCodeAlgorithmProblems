

nums1 = [2,3,5,12,13]
nums2 = [1,4,7]

if __name__ == '__main__':

    def compute_list_median(nums1,nums2):
        if nums1 == []:
            return nums2
        else:
            for k in range(len(nums2)):
                l = len(nums1)-1
                i = l
                while nums1[i] > nums2[k] and i>=0:
                    if i+1 > len(nums1)-1:
                        nums1.append(nums1[i])
                    else:
                        nums1[i+1] = nums1[i]
                    i = i -1
                if i + 1 > len(nums1) - 1:
                    nums1.append(nums2[k])
                else:
                    nums1[i + 1] = nums2[k]
            return nums1

    def compute_mean(list_num):
        print(list_num)
        print(len(list_num)//2)
        if len(list_num ) % 2 == 0:
            temp_index = len(list_num)//2
            return (list_num[temp_index] + list_num[temp_index-1])/2
        elif len(list_num)% 2  == 1:
            temp_index = len(list_num)//2
            return (list_num[temp_index])

    # print(compute_list_median(nums1,nums2))
    print(compute_mean(compute_list_median(nums1,nums2)))

