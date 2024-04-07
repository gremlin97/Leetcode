/**
 * @return {Function}
 */
var createHelloWorld = function() {
    greeting = 'Hello World';
    return function() {
        return greeting;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */