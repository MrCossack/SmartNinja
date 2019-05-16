name = "wert"
name2 = int(input("Tippe eine Zahl ein: \n"))
name3 = 2.0
#comment
if name2 == 3 or name2 == 8:
    print ("yeah")
else:
    print("nope")

#print (8%2 == 0)
# + - / *
# % modulo - Rest einer Division

count = 10
while(count):
    print(count)
    count -= 1

    if count < 5:
        #break
        continue

    print("continue text")

bundesL = ["Wien", "Burgenland", "Niederoesterreich"]
#print (range(0, 4 , 2))
for item in bundesL:
    print (item)

