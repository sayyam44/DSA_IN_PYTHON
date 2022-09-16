def repeated_char(s):
    h={}
    for i in range(len(s)):
        h[s[i]]=1+h.get(s[i],0)
        for j in range (len(s)):
            if h[s[j]]>1:
                return s[j]