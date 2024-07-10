def twoSum(nums, target):

        index = {}

        for i,numero in enumerate(nums):
            complemento = target - numero
            if complemento in index:
                return(index[complemento],i)
            index[numero] = i

        return None
    