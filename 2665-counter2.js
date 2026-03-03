var createCounter = function(init) {
    var currentvalue=init;
    return{
        increment:function(){
            return ++currentvalue
        },
        decrement:function(){
            return --currentvalue
        },
        reset:function(){
            currentvalue=init
            return currentvalue
        },
    }
    
};