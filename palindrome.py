def checplindrome(n):
    if str(n)==str(n)[::-1]:
        return "Is Plindrome"
    else:
        return "Not plindrome"

print(checplindrome(121))