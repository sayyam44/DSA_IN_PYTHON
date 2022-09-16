# https://leetcode.com/problems/longest-common-prefix/
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
def lng(strs):
    m,M=min(strs),max(strs)
    for i,ch in enumerate(m):
        if ch!=M[i]:
            return m[:i]
    return m