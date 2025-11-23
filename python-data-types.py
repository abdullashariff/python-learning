class DataTypes:

    def _init_(self):
        print('inside constructor')

    def sum(self, x, y):
            self.x = x
            self.y = y
            return x+y

obj = DataTypes()

print(obj.sum(2,4))
my_list = [2, 3, 5, 7, 11]

list = [1,2,4,5,6]
list2 = [x*x for x in list]
print(list2)


list = [2,4,5]
for x in range(5, 8, 2):
     print(x)


dictionary = {"name": 'abd', "age": 23}
print(dictionary["name"])

del dictionary["name"]
print(f"age : {dictionary["age"]}")

dictionary['firstname'] = 'ab'

print(dictionary)


str = 'polindrome'
strReverse = str[::-1]
print(f"is string polindrome {str } ? {strReverse == str}")

str = 'aabbbaa'
strReverse = str[::-1]
print(f"is string polindrome {str } ? {strReverse == str}")