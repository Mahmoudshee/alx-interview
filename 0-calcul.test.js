// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber function', () => {
    it('should round and sum two numbers', () => {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should round and sum numbers with decimals', () => {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
});

