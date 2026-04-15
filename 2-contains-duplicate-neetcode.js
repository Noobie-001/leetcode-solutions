class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        for (let i=0; i< nums.length; i++){
            for (let j=i+1; j<nums.length; j++){
                if (nums[i]===nums[j]){
                    return true
                }
            }
        
        }
        return false
    }
}
// more optimal way
class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const set= new Set(nums)
        if (set.size!==nums.length){
            return true
        }
        return false
    }
}

