#Challenge 2

In the block of text below, find the longest substring that is the same in reverse (palindrome). As an example, if the input was "Ilikeracecarsthatgofast" the answer would be "racecar".

Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv
edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi
nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo
ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft
hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto
getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco
nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco
nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre
memberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed
edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI
tisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore
ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevoti
onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod
shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh
allnotperishfromtheearth

_______________________________________________
Code:

def longest_palindrome_substring(s):
    n = len(s)
    start = 0
    max_length = 1

    for i in range(1, n):
        # Check for odd length palindromes
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # Check for even length palindromes
        low = i - 1
        high = i
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

    return s[start:start + max_length]

# Given text
text = """
Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv
edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi
nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo
ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft
hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto
getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco
nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco
nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre
memberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed
edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI
tisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore
ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevoti
onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod
shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh
allnotperishfromtheearth
"""

# Remove newline characters and spaces
text = ''.join(text.split())

# Find the longest palindrome substring
result = longest_palindrome_substring(text)
print(result)