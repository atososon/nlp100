s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans=[]
s2=s.split(" ")
for i in s2:
    ans.append(len(i) - i.count(',') - i.count('.'))
print(ans)