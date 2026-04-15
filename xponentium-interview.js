class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length!==t.length){
            return false
        }
        if (s.split('').sort().join('')===t.split('').sort().join('')){
            return true
        }
        return false
    }
}
// more optimal way
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length!==t.length){
            return false
        }
        const count={}
        for (let i=0; i<s.length; i++){
            count[s[i]]=(count[s[i]] || 0)+1
            count[t[i]]=(count[t[i]] || 0)-1
        }
        for (let key in count){
            if (count[key]!==0){
                return false
            }
        }
        return true
    }
}       

// 3rd way optimal and easier to understand
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let count={}
        if (s.length!==t.length){
            return false
        }
        for(let char of s){
            count[char]=(count[char]||0) +1
        }

        for (let char of t){
            if(!count[char]){
                return false
            }
            count[char]-=1
            
        }
        return true
        
        
    }
}
