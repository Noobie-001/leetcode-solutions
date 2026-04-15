class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        ans=[...nums,...nums]
        return ans
    }
}
// 2nd way not optimal but works
class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let ans=[]
        ans.push(...nums)
        ans=ans.concat(nums)
        return ans
    }
}