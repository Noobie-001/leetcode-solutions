var removeDuplicates = function(nums) {
    let unique=[]
    for(let i = 0; i<nums.length;i++){
        if(!unique.includes(nums[i])){
            unique.push(nums[i])
        }
    }
    for (let i = 0; i < unique.length; i++) {
        nums[i] = unique[i];
    }
    return unique.length
};