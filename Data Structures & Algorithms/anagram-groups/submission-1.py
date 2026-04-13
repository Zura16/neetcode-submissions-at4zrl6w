class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        answer = []

        # ["act","pots","tops","cat","stop","hat"]
        for phrase in strs:

            # "act" it1
            # "pots" it2
            # "tops" it3
            #  "cat" it4
            temp = ''.join(sorted(phrase)) # ["c","a","t"] -> ["a","c","t"]
            print(temp)
            # "act" it1
            # "opst" it2
            # "opst" it3
            # "act" it4
            # "opst" it5
            # "aht" it6


            if temp in dic:
                dic[temp].append(phrase)
            else:
                # {"act":["act"]} it1
                # {"act":["act"],"opst":["pots"]} it2
                dic[temp] = [phrase]
        
        # {"act":["act", "cat"],"opst":["stop", "pots", "tops"],"aht":["hat"]}
        for li in dic.values():
            # dic.values() -> [["act", "cat"],["stop", "pots", "tops"],["hat"]]
            answer.append(li)
        
        return answer