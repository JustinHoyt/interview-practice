import { describe, expect, it } from "bun:test";
import { jump } from "./0045_jump_game_II";

describe("Jump game II", () => {
  it("should pass default case 1", () => {
    expect(jump([2, 3, 1, 1, 4])).toEqual(2);
  });

  it("should pass default case 2", () => {
    expect(jump([2, 3, 0, 1, 4])).toEqual(2);
  });

  it("should not count out of bounds as finished", () => {
    expect(jump([2, 3, 40, 1, 4])).toEqual(2);
  });

  it("should return 0 for an empty array", () => {
    expect(jump([])).toEqual(0);
  });

  it("should run at max length array", () => {
    expect(jump(Array(10_000).fill(5))).toEqual(2000);
  });
});
