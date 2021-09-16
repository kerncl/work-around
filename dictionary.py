#Dictionary
post = {"user_id": 209, "message": "D5 E5 C5", "language": "English", "datatime": "20230216T12431Z", "location": (44.590533, -104.71556)}
#add a new set of data
post['state']="Penang"
#Access the value
print(post['state'])
#option 1
if 'location' in post:
    print(post['location'])
else:
    print("The post doesnt contain a location value")
#option 2
try:
    print(post["abc"])
except KeyError:
    print("THe post does not have a location")
#option 3
post.get('location')

#print all value of keys
#option 1
for key in post.keys():
    value = post.get(key)
    #value = post[key]
    print(key, "=", value)
#option 2
for key, value in post.items():
    print(key, "=", value)


