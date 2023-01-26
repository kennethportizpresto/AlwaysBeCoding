def helperFunc(character:str) -> bool:
    ''' determines if a lowercase or capital character is part of the alphabet '''
    return (ord('a') <= ord(character) <= ord('z') or
            ord('A') <= ord(character) <= ord('Z'))

def reverse(myStr:str) -> str:
    ''' returns a reversed string but special characters are not affected '''
    myStr = list(myStr)
    lptr, rptr = 0, len(myStr) - 1
    res = ""
    while(lptr < rptr):
        if helperFunc(myStr[lptr]) and helperFunc(myStr[rptr]): 
            myStr[lptr], myStr[rptr] = myStr[rptr], myStr[lptr]
            lptr += 1
            rptr -= 1 
        elif not helperFunc(myStr[lptr]) and helperFunc(myStr[rptr]): 
            lptr += 1 
        elif helperFunc(myStr[lptr]) and not helperFunc(myStr[rptr]): 
            rptr -= 1
        else:
            lptr += 1
            rptr -= 1
    for i in myStr:
        res += i
    return res     

if __name__== "__main__":
    try:
        assert reverse("a,b$c") == "c,b$a", "TestCase 1: Strings Do Not Match"
        assert reverse("Ab,c,de!$") == "ed,c,bA!$", "TestCase 2: Strings Do Not Match"
        print("Process finished with exit code 0")
    except AssertionError as a:
        print(a)
        print("Process finished with exit code 1")
# Time complexity: O(a)
# Space complexity: O(a)
