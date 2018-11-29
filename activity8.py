import csv

class Customer:
    customers = []

    def __init__(self, id, first_name, last_name, company_name, address, city, state, zip):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        Customer.customers.append(self)


    

def display_title():
    # print title
    print("Customer Viewer")

def csv_reader():
    headerRow = True
    # open file in read mode
    with open("customers.csv","r",newline="") as file:
        # new csv reader
        reader = csv.reader(file)
        # for each record
        for record in reader:
            # skip the header row
            if headerRow:
                headerRow = False
                continue
            else:
                #if its not empty
                if str.strip(record[0]) != "":
                    #create new result
                    Customer(int(record[0]), record[1], record[2], record[3], record[4], record[5], record[6], record[7])

def find_customer(cust_id):
    found = False
    # for all the results
    for customer in Customer.customers:
        # if the id matches
        if(customer.id == cust_id):
            # return the string to print
            print("\n{:s} {:s}\n{:s}\n{:s}, {:s} {:s}".format(customer.first_name, customer.last_name, customer.address, customer.city, customer.state, customer.zip))
            found = True
    if found == False:
        print("\nNo customer with that ID.")
        


def main():
    display_title()
    csv_reader()

    keep_going = True

    while keep_going:
        cust_id = int(input("\nEnter Customer ID: "))
        find_customer(cust_id)

        response = ""
        while response == "":
            response = input("\nContinue? (y/n): ")
            if response == "y":
                break
            elif response == "n":
                keep_going = False
                print("\nBye!")
                continue
            else:
                print("Invalid Option")
                response = ""
                continue
        

if __name__ == '__main__':
    main()




