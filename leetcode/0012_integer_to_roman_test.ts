import { describe, expect, it } from "bun:test";
import { intToRoman } from "./0012_integer_to_roman";

describe("Integer to roman", () => {
  it("should use subtractive form for fours and nines", () => {
    const actual = intToRoman(49);
    const expected = "XLIX";

    expect(actual).toEqual(expected);
  });

  it("should use additive form for digits [1, 3, 7]", () => {
    const actual = intToRoman(137);
    const expected = "CXXXVII";

    expect(actual).toEqual(expected);
  });

  it("should use additive form for digits [3, 2, 8, 6]", () => {
    const actual = intToRoman(3286);
    const expected = "MMMCCLXXXVI";

    expect(actual).toEqual(expected);
  });

  it("should work on max constrant 3999", () => {
    const actual = intToRoman(3999);
    const expected = "MMMCMXCIX";

    expect(actual).toEqual(expected);
  });

  it("should output MCMXCIV for 1994", () => {
    const actual = intToRoman(1994);
    const expected = "MCMXCIV";

    expect(actual).toEqual(expected);
  });
});
