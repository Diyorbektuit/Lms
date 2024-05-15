thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2 = {
  "brand": "Chevrolet",
  "model": "Camaro",
  "year": 2010
}
thislist = [thisdict]
thislist.append(thisdict2)
print(thislist)
for item in thislist:
  brand = item["brand"]
  print(brand)