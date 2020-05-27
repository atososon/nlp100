def n_gram(s,n):
    return [s[i:i+n] for i in range(len(s)-n+1)]
text = "I am an NLPer"
print(n_gram(text.split(),2))
print(n_gram(text,2))