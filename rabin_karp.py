import random


def poly_hash(s, x, prime):
    hash = 0
    for char in reversed(s):
        hash = (hash * x + ord(char)) % prime
    return hash


def rabin_karp(s, t):
    prime = 1000000007
    x = random.randint(1, prime - 1)

    positions = []
    hash = poly_hash(t, x, prime)
    S, T, y = len(s), len(t), 1
    H = [0] * (S - T + 1)

    if T > S:
        return positions

    for _ in range(T):
        y = (y * x) % prime
    H[S - T] = poly_hash(s[(S - T):], x, prime)

    for i in range(S - T - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(s[i]) - (y * ord(s[i + T]))) % prime

    for i in range(S - T + 1):
        if hash == H[i] and s[i:i + T] == t:
            positions.append(i)

    return positions


# Tests

# Test case 1: Pattern at the beginning
assert rabin_karp("hello", "he") == [0], "Test case 1 failed"

# Test case 2: Pattern at the end
assert rabin_karp("hello", "lo") == [3], "Test case 2 failed"

# Test case 3: Pattern in the middle
assert rabin_karp("hello", "el") == [1], "Test case 3 failed"

# Test case 4: No match
assert rabin_karp("hello", "world") == [], "Test case 4 failed"

# Test case 5: Multiple matches, non-overlapping
assert rabin_karp("abracadabra", "abra") == [0, 7], "Test case 5 failed"

# Test case 6: Multiple matches, overlapping
assert rabin_karp("aaa", "aa") == [0, 1], "Test case 6 failed"

# Test case 7: Match entire string
assert rabin_karp("hello", "hello") == [0], "Test case 7 failed"

# Test case 8: Pattern longer than text
assert rabin_karp("short", "longerthan") == [], "Test case 8 failed"

# Test case 9: Matching with special characters
assert rabin_karp("sp3c!@l_ch@rs", "_ch@") == [7], "Test case 9 failed"

# Test case 10: Case sensitivity, no match
assert rabin_karp("CaseSensitive", "casesensitive") == [], "Test case 10 failed"

# Test case 11: Empty string and pattern
assert rabin_karp("", "") == [0], "Test case 11 failed"

# Test case 12: Empty string, non-empty pattern
assert rabin_karp("", "nonempty") == [], "Test case 12 failed"

# Test case 13: Non-empty string, empty pattern
assert rabin_karp("nonempty", "") == [0, 1, 2, 3, 4, 5, 6, 7, 8], "Test case 13 failed"