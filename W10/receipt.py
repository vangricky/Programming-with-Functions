import csv
import datetime

def main():
    try:
        products_dict = read_dictionary("./Lesson9/products.csv", "rt")
        print("Walmart")
        print()
        read_requests("./Lesson9/request.csv", products_dict)
        print()
    
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("File not found.")
    except (csv.Error, KeyError) as error:
        print(f"CSV file/files not formatted correctly.")



def read_requests(filename, products_dict):   
    with open(filename, "rt") as request_file:
        quantity = 0
        sub_total = 0
        reader = csv.reader(request_file)
        next(reader)
        for line in reader:
            item_details = products_dict[line[0]]
            quantity += int(line[1])
            sub_total += float(item_details[1]) * int(line[1])
            print(f"Name: {item_details[0]}, Quantity: {line[1]}, Price: ${item_details[1]}")
        print()
        print(f"Amount of items purchased {quantity}")
        print(f"Sub total: ${sub_total:.2f}")
        sales_tax = sub_total * .06
        print(f"Tax: ${sales_tax:.2f}")
        amount_due = sales_tax + sub_total
        print(f"Total amount due: ${amount_due:.2f}")
        print()
        print("Thank you for your service!")
        date = datetime.datetime.now()
        print(date)
        print()
        print("Please fill out our online survey at Survey.org.com/survey.")
    return

    

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, "rt") as products_file:
        
        reader = csv.reader(products_file)
        next(reader)
        key_column_index = 0
        for row_list in reader:
            if len(row_list) != 0:  
                key = row_list[key_column_index]
                dictionary[key] = row_list[1:]
    return dictionary

if __name__ == "__main__":
    main()