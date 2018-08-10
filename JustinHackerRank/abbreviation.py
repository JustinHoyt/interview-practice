def abbreviation_rec(s1, s2, memo):
    pass


def abbreviation(s1, s2):
    memo = {}
    return abbreviation_rec(s1, s2, memo)


s1 = "AbcDE"
s2 = "ABDE"
print(abbreviation(s1, s2))
