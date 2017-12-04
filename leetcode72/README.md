# 72. Edit Distance

## Statement
s1 = [0...len1-1]<br/>
s2 = [0...len2-1]

dp[i][j] means how many steps convert [0...i-1] to [0...j-1].

We traverse possible cases at the string1.


## Boundary
Converting from An arbitrary string(s1) to an empty string(s2) consumes length of s1 steps by deleting from s1 which is same as an empty string to an arbitrary string.

So, dp[i][0]=i, dp[0][j]=j

## General
We define (i1,j1) <= (i2,j2), if i1 <= i2 and j1 <= j2.<br/>
When we consider dp[i][j], suppose dp[i1][j2] which (i1,j2) <= (i,j) has already be computed.

- s1[i-1]==s2[j-1], last char of each string is same. dp[i][j]=dp[i-1][j-1]

If s1[i-1]!=s2[j-1], 3 ways can be applied.
- replacement, the same as deletion of last char of both strings, so this problem down into problem of s1[0...i-2] and s2[0...j-2], dp[i][j]=dp[i-1][j-1]+1
- deletion, delete the last char of s1, so dp[i][j]=dp[i-1][j]+1
- insertion, insert a char having the value of s2[0...j-1] at the tail of s1, so dp[i][j]=dp[i][j-1]+1

## Conclusion
- dp[i][0] = i;
- dp[0][j] = j;
- dp[i][j] = dp[i - 1][j - 1], if word1[i - 1] = word2[j - 1];
- dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1), otherwise.

## Think
In this problem, we need to consider many arguments.
- What position to operate in s1
- Which operation type to select 
- What value to select, if deside to insert

It means, we need to consider a tuple(index, type, value?) at the same time. Thus, we only operate at the tail of substring of s1 along with substring of s2. 


