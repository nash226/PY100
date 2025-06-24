grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

def list_remove(a):
    for item in a[:]:
        a.remove(item)
        print (item)

list_remove(grocery_list)

print(grocery_list)
