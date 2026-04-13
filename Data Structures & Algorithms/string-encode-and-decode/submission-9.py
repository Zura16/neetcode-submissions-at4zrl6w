class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for ele in strs:
            s += str(len(ele)) + '#' + ele
        return s
            

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            lenght = ""
            while s[i] != '#':
                lenght += s[i]
                i += 1
            i += 1
            lenght = int(lenght)
            newword = ''
            while lenght > 0:
                newword += s[i]
                i += 1
                lenght -= 1
            output.append(newword)
        return output
            
            

