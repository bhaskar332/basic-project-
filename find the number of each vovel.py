vowels = 'aeiou'
ip_str = 'hello, have you tried our tutorial section yet'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
    if char in count:
        count[char] += 1
print(count)

#Using dictionary and list comprehension

ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str = ip_str.casefold()

count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)