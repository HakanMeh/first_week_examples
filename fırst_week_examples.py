#Adding keys and values to the dictionary
person = {
    "name": "John",
    "age": 30
}

person["email"] = "john@example.com"  # Yeni anahtar ve değeri eklemek
print(person)


#Averaging
not1=55
not2=100
ort=(not1+not2)/2
print("not1 {},not2 {},ort {}".format(not1,not2,ort))


#medyan
number1 = int(input("number1"))
number2=int(input("number1"))
number3=int(input("number1"))

medyan=(number1+number2+number3)/3
print(medyan)


#multiplication table for a number
number=int(input("sayı"))
for i in range(1,10):
    print(number ,"x", i,"=" ,i*number)


#Numbers divided by 3 and 4 exactly.
for i in range(100):
    if i%3==0 and i%4==0:
        print(i)

#Write all the numbers of the number divided by
sayı=int(input("sayı gır"))
for i in range(1,sayı+1):
    if sayı%i==0:
        print(i)

#Simple Format Method
ad=input("adınız")
soyad=input("soyad")
yas=int(input("yasınz"))
print("adınız{} soyadınız {} yasınız {}".format(ad,soyad,yas))


# Add fılm dıctıonary
# Initialize an empty movie collection
movies = []
movie1 = {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'genre': 'Sci-Fi'}
movie2 = {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'year': 1994, 'genre': 'Drama'}

movies.append(movie1)
movies.append(movie2)

for movie in movies:
    print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}, Genre: {movie['genre']}")



#The game of number prediction
number=4
number_predictions=0
while True:
    guess = int(input("guess:"))
    number_predictions +=1
    if number==guess:
        print("true")
        print("How many predictions did you find the result of",number_predictions)
        break

    elif number>guess:
        print("type larger number please")
    elif number<guess:
        print("write a smaller number please ")