### Resources
- https://leetcode.com/discuss/study-guide/1405817/backtracking-algorithm-problems-to-practice
- https://www.youtube.com/watch?v=Zq4upTEaQyM

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

```
bool backtracking(configuration conf) {
    //base case
    if (no more choices):
        return true
    else
        return false

    for (all available choices) {
        //make a choice c

        make one choice c and update conf

        status = backtracking(updated conf)

        if (status is true)
            execute some logics
        else
            unmake the choice c and revert to old conf
    }

    return false
}
```

State - essentially a backtracking problem is asking you to find valid states
incrementally build candidates to solutions and abandons any (partial) candidate if determined that candidate cannot be valid.