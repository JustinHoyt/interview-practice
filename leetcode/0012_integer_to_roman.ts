export function intToRoman(num: number): string {
  let roman = "";
  for (let magnitude = 0; magnitude < String(num).length; magnitude++) {
    const digit = (num / 10 ** magnitude) % 10;
    const partialNum = digit * 10 ** magnitude;
    num -= partialNum;
    // subtractive form
    if (digit === 4 || digit === 9) {
      if (partialNum === 4) {
        roman = "IV" + roman;
      } else if (partialNum === 9) {
        roman = "IX" + roman;
      } else if (partialNum === 40) {
        roman = "XL" + roman;
      } else if (partialNum === 90) {
        roman = "XC" + roman;
      } else if (partialNum === 400) {
        roman = "CD" + roman;
      } else if (partialNum === 900) {
        roman = "CM" + roman;
      }
    } // additive form
    else {
      if (partialNum < 5) {
        roman = "I".repeat(digit) + roman;
      } else if (partialNum < 10) {
        roman = "V" + "I".repeat(digit - 5) + roman;
      } else if (partialNum < 50) {
        roman = "X".repeat(digit) + roman;
      } else if (partialNum < 100) {
        roman = "L" + "X".repeat(digit - 5) + roman;
      } else if (partialNum < 500) {
        roman = "C".repeat(digit) + roman;
      } else if (partialNum < 1000) {
        roman = "D" + "C".repeat(digit - 5) + roman;
      } else {
        roman = "M".repeat(digit) + roman;
      }
    }
  }
  return roman;
}
