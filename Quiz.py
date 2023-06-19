
subjects = {"History", "Science", "English","Anime","Math","Cartoons"}


print("Hello, Welcome to the quiz of Knowled. This quiz will test you on a variety of topics.\n")
print("What topic will you choose?\n")

for i in subjects:
    print (i)

print("\n")

choice = input().lower()
print("\n")
for j in subjects:
  if choice == j.lower():
    print("You chose {}".format(j))

print("\n")





