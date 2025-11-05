class Solution(object):#s here is called string
    def isValid(self, s):
        open_bracket=['(','{','[']
        close_bracket=[')','}',']']
        d=dict(zip(close_bracket,open_bracket))#d = dict(zip(...)) — makes a dictionary that maps each closing bracket to its matching opening bracket
        if (s[0] in close_bracket or s[-1] in open_bracket):#If the first character is a closing bracket (bad) or the last is an opening bracket (also bad), the string cannot be valid, so we return False immediately
            return False
        ind=0
        result=[]
        while (ind<len(s)):
            if(s[ind]in open_bracket):
                result.append(s[ind])

            else:#s[ind] is the current closing bracket, like ')' or ']'.The dictionary d maps each closing bracket to the opening one it needs
                need=d[s[ind]]
                if(len(result)>0 and result[-1]==need):#result[-1] means the last element in the list, i.e. the top of the stack.== need checks if that top element matches the required opening bracket.greater than zero means check that the stack is not empty
                    result.pop()
                else:
                     return False
            ind+=1
        if(len(result)==0):#jodi son opening closing peye jai match then stack empty mane successfully runed!!
            return True 
        else:
            return False
        