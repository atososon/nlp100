s = """Hi He Lied Because Boron Could Not Oxidize Fluorine.
New Nations Might Also Sign Peace Security Clause. Arthur King
Can."""
a = s.split()
ans = {}
for i in range(len(a)):
    if i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18:
        a[i] = a[i][0]
    else:
        a[i] = a[i][:2:]
    ans[a[i]] = i+1
print(ans)