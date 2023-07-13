### Resources
- https://leetcode.com/discuss/study-guide/1405817/backtracking-algorithm-problems-to-practice

**Template**
```
void backtrack(arguments) {
    if (condition == true) {
        result.push_back(current);
        return;
    }

    for (int i = num; i <= last; i++) {
        current.push_back(i) //explore candidate
        backtrack(arguments);
        current.pop_back(); //abandon candidate
    }
}
```

