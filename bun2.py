import requests,json
from pprint import pprint


# with open("r.json","w",encoding="UTF-8") as file:
#     a=json.dump(headers,file)
# with open("r.json","r",encoding="UTF-8") as file:
#     A=json.load(file)

# print(A,type(A))




# variable=requests.Session()
# cokies={"qwerty":"123234234"}
# headers={"User-Agent":"Bunyod"}
# response=requests.head("https://httpbin.org/cookies",cookies=cokies)
# print(response.status_code)
# print(response.text)





url = "https://fakestoreapi.com/products"

# url_2 ="https://httpbin.org"


# data = {
#     "title": "Partially updated title"
# }


response=requests.get(url=url)
# print(response.url)

# with open("r.json","w",encoding="UTF-8") as file:
#     json.dump(response.json(),file,indent=4)
# with open("r.json","r",encoding="UTF-8") as file:
#     a=json.load(file)
dict_=response.json()
# pprint(response.json()[0]["image"])
for i in dict_:
    print(i["id"],".",i["title"],"---",i["price"])
id_=int(input("id: "))

image=requests.get(url=response.json()[id_-1]["image"])
with open("image/l.png","wb") as file:
    file.write(image.content)




