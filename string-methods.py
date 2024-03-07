text = "abcdefghijklmnop"

print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)
print("bannannnnaa".count("n"))
print("bannnananaan".index("b"))
print("bananabananabanana".replace("ana", "XXYZZ"))

sentance = "Hello, kind-sir; how many! I be of service today?"
punctuation = ".,;!?-"
for p in punctuation:
    sentance = sentance.replace(p, "")
print(sentance)

print("THIS IS A SENTANCE AND I WANT THE WORDS".split(" "))

text = "Bob goes to school. Bob like to play tennis. I am friends with Bob. Such a nice guy Bob "
print(text.find("Bob"))
print(text.rfind("Bob"))

i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1
