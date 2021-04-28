from itertools import islice, zip_longest

tutors = ["Пётр", "Марина", "Семён", "Галина", "Джон", "Анна", "Дженифер"]
klasses = ["5a", "6г", "7а", "5б", "8а" , "9в", "10а"]

rezult = (i for i in zip_longest(tutors, klasses))

print(type(rezult))
print(*islice(rezult, 9))