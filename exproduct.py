def product(s):
    exclaim_cnt = 0
    question_cnt = 0
    for i in s:
        if i == "!":
            exclaim_cnt += 1
        else:
            question_cnt += 1
    return exclaim_cnt * question_cnt

print product('')
print product('!')
print product('!!??!!')

# blah blah
