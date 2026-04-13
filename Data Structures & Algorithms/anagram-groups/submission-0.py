class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           
           #s=[]
           #for i in List:
             #if len(i)==len(yo)
             #yo=s.add[i]
        #List, dict
        anagram = list()
        anagramdict = dict()

        #iterate over strs
        for string in strs:
            sortedString = "".join(sorted(string))
            #print(sortedString) #sort every element
            anaList = anagramdict.get(sortedString)

            if anaList is None:
                anagramdict[sortedString] = []
            anagramdict[sortedString].append(string) #feed into dictionary with sorted as key and element as value

        #print(anagramdict)

        #append values of dictionary into list
        for sortedString in anagramdict:
            anagram.append(anagramdict[sortedString])

        #return list
        return anagram

    
             
            
     
        