product_name = []
product_price = []
product_id = []

def add_pro():
    name = input('Please give the product name: ')
    try:
        price = float(input('Please give the product price: '))
        id = int(input('Please give the product id (should be Unique and format is just integers): '))
    except ValueError:
        print('Please enter a valid number')
        return
    if id not in product_id:
        product_name.append(name)
        product_price.append(price)
        product_id.append(id)
        print('Product added successfully')
    else:
        print(f'The product id ({id}) already exists')
def display_pro():
    for i in range(len(product_name)):
        print(f'Product{i +1 }  ==> Name: {product_name[i]} ***  Price : {product_price[i]} *** ID : {product_id[i]}')
def remove_pro():
    try:
        rem = int(input('Please enter ID of the product you want to remove: '))
    except ValueError:
        print('Please enter a valid number')
        return
    if rem in product_id:
        index = product_id.index(rem)
        product_id.pop(index)
        product_name.pop(index)
        product_price.pop(index)
        print('Product removed successfully')
    else:
        print('Product not found')
def edit_pro():
    try:
        edit = int(input('Please enter ID of the product you want to edit: '))
    except ValueError:
        print('Please enter a valid number')
        return
    if edit in product_id:
        index = product_id.index(edit)
        n_name = input('Please give the product name: ')
        if n_name:
            product_name[index] = n_name
        n_price_input = input('Please give the product price: ')
        if n_price_input:
            try:
                n_price = float(n_price_input)
                product_price[index] = n_price
            except ValueError:
                print('Invalid price entered, keeping the previous price.')
        print('Product edited successfully')
    else:
        print('Product not found')
def search_pro():
    try:
        search = int(input('do you want to Search with Name(1) or ID(2)? : '))
    except ValueError:
        print('Please enter a valid number')
        return
    if search == 1:
        name = input('Please enter the name of the product you want to search: ')
        if name in product_name:
            index = product_name.index(name)
            print(f'Product ==> Name: {product_name[index]} ***  Price : {product_price[index]} *** ID : {product_id[index]}')
        else:
            print('Product not found')
    elif search == 2:
        id = int(input('Please enter the ID of the product you want to search: '))
        if id in product_id:
            index = product_id.index(id)
            print(f'Product ==> Name: {product_name[index]} ***  Price : {product_price[index]} *** ID : {product_id[index]}')
        else:
            print('Product not found')
    else:
        print('Invalid input')
def detail():
    number_pro = len(product_name)
    value_pro = sum(product_price)
    print(f'Total number of products: {number_pro}')
    print(f'Total value of products: {value_pro}')
def help():
    print('"ADD Product" is used to add a product to the list')
    print('"DISPLAY Product" is used to display all products in the list')
    print('"REMOVE Product" is used to remove a product from the list')
    print('"EDIT Product" is used to edit a product in the list')
    print('"SEARCH Product" is used to search for a product in the list')
    print('"DETAIL" is used to display the total number of products and the total value of products')


while True:
    print('\t ***Welcome to the Product Management System***')
    print('\t\t1. Add Product')
    print('\t\t2. Display Product')
    print('\t\t3. Remove Product')
    print('\t\t4. Edit Product')
    print('\t\t5. Search Product')
    print('\t\t6. Detail')
    print('\t\t7. Help')
    print('\t\t8. Exit')
    try:
        choice = int(input('What is your choice?  :  '))
    except ValueError:
        print('Please enter a valid number')
        continue
    if choice == 1:
        add_pro()
    elif choice == 2:
        display_pro()
    elif choice == 3:
        remove_pro()
    elif choice == 4:
        edit_pro()
    elif choice == 5:
        search_pro()
    elif choice == 6:
        detail()
    elif choice == 7:
        help()
    elif choice == 8:
        print('Thank you for using the Product Management System')
        break
    else:
        print('Please enter a valid number')
        continue


