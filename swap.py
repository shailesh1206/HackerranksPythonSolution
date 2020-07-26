def swap_case(s):
    g = []
    for i in range(len(s)):
        if s[i].isupper():
            g.append( s[i].lower())
        elif s[i].lower():
            g.append( s[i].upper())
    p = ""
    return p.join(g)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
