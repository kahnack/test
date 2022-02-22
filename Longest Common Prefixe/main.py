# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.



class Solution:
    # Ma solution
    def longestCommonPrefix(self, strs: list) -> str:
        res = ''
        n = 0 # position lettre

        stop = False
        while not stop:
            if n < len(strs[0]):
                res += strs[0][n]
            else:
                print('break')
                break
            print(f'res: {res}')

            for i in range(len(strs)):
                print(f'mot = {strs[i]}')
                print(f' i vaut {i} et n vaut {n}')
                print(f'len(strs[i]: {len(strs[i])}')
                if n < len(strs[i]):
                    print(f'strs[i][n]: {strs[i][n]}')
                    print('prout')
                    if strs[i][n] == res[n]:
                        print('ok')

                        continue
                    else:
                        if len(res) == 1:
                            print('ko')
                            res = ''
                        else:
                            print('fini')
                            res = res[:-1]
                        print('stop')
                        stop = True
                        break
                else:
                    if len(res) == 1:
                        print('ko')
                        res = ''
                    else:
                        print('fini')
                        res = res[:-1]
                    print('stop')
                    stop = True
                    break
            print('n+1')
            n += 1


        return res

    # Stackoverflow 1
    def longestCommonPrefix2(self, strs: list) -> str:
        prefix = ""
        if len(strs) == 0: return prefix

        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                prefix += c
            else:
                break
        return prefix

    # Stackoverflow 2
    def longestCommonPrefix3(self, strs: list) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]

        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                p += x
            else:
                break
        return p

input = ["flower","flow","flight"]
print(f'Output 1: {Solution().longestCommonPrefix3(input)}')

input = ["dog","doge","dogero", "dogejife", "dogtest"]
print(f'Output 2: {Solution().longestCommonPrefix3(input)}')

input = ["ba", "bca"]
print(f'Output 3: {Solution().longestCommonPrefix3(input)}')


# input = ["flower","flow","flight"]
# print(Solution().longestCommonPrefix(input))


