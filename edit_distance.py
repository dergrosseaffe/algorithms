def edit_distance(s1, s2):
    cache = {}

    def recurse(m, n):
        if (m, n) in cache:
            return cache[(m, n)]

        if m == 0:
            return n
        if n == 0:
            return m
        if s1[m-1] == s2[n-1]:
            return recurse(m-1, n-1)

        result = 1 + min(recurse(m-1, n),    # delete
                         recurse(m, n-1),    # insert
                         recurse(m-1, n-1))  # replace

        cache[(m, n)] = result
        return result

    return recurse(len(s1), len(s2))


print(edit_distance('kitten', 'sitting'))
print(edit_distance('a cat!', 'two cats!'))
print(edit_distance('o rato roeu a roupa do rei de roma', 'a roupa do rato de roma roeu o rei'))
