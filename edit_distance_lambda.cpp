#include <iostream>
#include <string>
#include <functional>

// Helper hash function for std::pair<size_t, size_t> to be used in std::unordered_map
struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &pair) const {
        auto hash1 = std::hash<T1>{}(pair.first);
        auto hash2 = std::hash<T2>{}(pair.second);
        return hash1 ^ hash2 << 1;
    }
};

size_t editDistance(const std::string& s1, const std::string& s2) {
    size_t m = s1.length();
    size_t n = s2.length();

    // Cache
    std::unordered_map<std::pair<size_t, size_t>, size_t, pair_hash> cache;

    // A Lambda for the recurrence relation
    std::function<size_t(size_t, size_t)> recurse;
    recurse = [&] (size_t m, size_t n) -> size_t {
        if (cache.contains({m, n})) return cache[{m, n}];

        if (m == 0) return n;
        if (n == 0) return m;
        if (s1[m-1] == s2[n-1]) return recurse(m-1, n-1);

        // No matches, so explores the three possible operations
        auto result = 1 + std::min({
            recurse(m, n-1),  // Insert
            recurse(m-1, n),  // Remove
            recurse(m-1, n-1) // Replace
        });

        cache[{m, n}] = result;
        return result;
    };

    return recurse(m, n);
}

int main() {
    std::cout << editDistance("a cat!", "two cats!") << std::endl;
    std::cout << editDistance("o rato roeu a roupa do rei de roma", "a roupa do rato de roma roeu o rei") << std::endl;
    return 0;
}
