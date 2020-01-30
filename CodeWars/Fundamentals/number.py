# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char. Examples input/output: XO("ooxx") => true XO("xooxx") => false XO(
# "ooxXm") => true XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true XO("zzoo") => false

def xo(s):
    x_num = 0
    o_num = 0
    for i in range(len(s)):
        if s[i].lower() == "x":
            x_num = x_num + 1
        elif s[i].lower() == "o":
            o_num = o_num + 1
    if x_num == o_num:
        return True
    else:
        return False


# best practice
# convert to lower and after  count the letter
def newXo(s):
    s = s.lower
    return s.count("x") == s.count("0")


print(xo("xxxQxoxGShoJomCoNLxxoxxbAoroxxdoUoExfvxxoxxptxxoxxko"))
