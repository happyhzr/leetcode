const reverseVowels = require("./main")

test('', () => {
    expect(reverseVowels("hello")).toBe("holle");
    expect(reverseVowels("leetcode")).toBe("leotcede");
});

