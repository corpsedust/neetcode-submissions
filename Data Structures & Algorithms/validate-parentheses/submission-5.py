class Solution:
   def isValid(self, s: str) -> bool:        
        st = []
        hashmap = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in hashmap and st:                   #c present in hashmap(key) and st not empty
                if st[-1] == hashmap[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return True if not st else False 



        
