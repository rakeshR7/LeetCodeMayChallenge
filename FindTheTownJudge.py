"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Examples:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


"""

import sys
from itertools import chain

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ele = collections.defaultdict(list)
        a = []
        
        for i in range(len(trust)):
            ele[trust[i][0]].append(trust[i][1])
            
        # print(ele)    
        x = list(chain(*ele.values()))
        # print(x)
        for i in range(1,N+1):
            if i not in ele.keys():
                print(i)
                print(x.count(i),N-1)
                if(x.count(i) == N-1):
                    return i
        
        return -1
                 
                                        
