class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["v","t","u"],
        "9":["w","x","y","z"]}
        combinations = [""]
        for digit in digits:
            new_comb = []
            for comb in combinations:
                for letter in d[digit]:
                    new_comb.append(comb+letter)
            combinations = new_comb
        return combinations