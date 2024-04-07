/**
 * @return {Function}
 */
var createHelloWorld = function() {
    // greeting = 'Hello World';
    // return function() {
    //     return greeting;
    // }
    
    // return () => 'Hello World';
    return (...args) => 'Hello World';
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */