def reduce_by_rules(lst, rules):
    while len(lst) > 1:
        for rule in rules:
            if len(lst) == 1:
                return lst[0]
            result = rule
            a = lst.pop(0)
            b = lst.pop(0)
            result = result(a, b)
            lst = [result] + lst
    return lst[0]



# test.it("Rules: [a + b, a - b]")
rules = [lambda a, b: a + b, lambda a, b: a - b]

lst = [2.0, 2.0, 3.0, 4.0]

print reduce_by_rules(lst, rules)
# should be 5.0

# test.it("Rules: [a + b]")
# rules = [lambda a, b: a + b]
#
# assert_equals(6.0, reduce_by_rules([2.0, 2.0, 2.0], rules))
# assert_equals(8.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(10.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(12.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], rules))
#
# test.it("Rules: [a + b, a - b, a * b]")
# rules = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b]
#
# assert_equals(2.0, reduce_by_rules([2.0, 2.0, 2.0], rules))
# assert_equals(4.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(6.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(4.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], rules))
#
# test.it("Rules: [min, max]")
# rules = [min, max]
#
# assert_equals(3.3, reduce_by_rules([1.3, 2.0, 3.3], rules))
# assert_equals(2.2, reduce_by_rules([4.1, 2.2, 2.1, 2.5], rules))
# assert_equals(8.0, reduce_by_rules([8.0, 8.1, 4.1, 12.0, 2.0], rules))
# assert_equals(2.4, reduce_by_rules([2.9, 2.8, 2.7, 2.6, 2.5, 2.4], rules))
