
def isPalindrome(text):
    for line in text:
        line = line.lower()
        line = line.strip()
        new_line = line.replace(' ', '')
        if new_line == new_line[::-1]:
            print (line)



def main ():

    text = open('32.txt')
    isPalindrome(text)

main()