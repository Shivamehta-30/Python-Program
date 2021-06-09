msg=input("Enter any string")
msg=list(msg)
msg.sort()
print(msg)
print(msg[::2])
msg_vo=[c for c in msg if c=='a' or c=='i' or c=='o' or c=='u' or c=='e']
print(msg_vo)
vo="aeiou"
for character in vo:
    print(character ," :",msg.count(character))