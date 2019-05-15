string = "i.like.this.program.very.much"
n = list(string.split("."))
print(n)
n = n[::-1]
print('.'.join(n))
