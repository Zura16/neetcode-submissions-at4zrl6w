class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check whether length is same or not 
        #if yes,[] check whether the characters are same or not.
        #anagram={}
        #if len(s)!=len(t): 
         #return False
         #race={r:1,a:1,c:1,e:1} = s
         #care={c:1,a:1,r:1,e:1} = t
        #s = collections.Counter(s)dict[key] = value

         #for char in s:

        anagram={}
        if len(s)!=len(t):
            return False
        hash_s=Counter(s)
        hash_t=Counter(t)
        for key in hash_s:
          if hash_s[key]!=hash_t[key]:
            return False
        return True
        
        
            

                 
        
        
         
           


      
         
        
         
        