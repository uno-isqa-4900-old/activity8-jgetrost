# Activity 8 - Object Oriented Python Exercise

## Objectives
Demonstrate your knowledge of how to develop an object oriented python program that reads information from a file.

## Directions
1. You will be developing a Customer Viewer application. The program will reads a list of Customer objects from a CSV file and allows the user to enter the data for a customer by specifying the customer’s ID. Here is what it looks like when running in the console:

![activity8-output](https://github.com/uno-isqa-4900/activity8/blob/master/images/activity8-output.png)

2. Download the [Customer CSV file](https://github.com/uno-isqa-4900/activity8/blob/master/data/customers.csv).

3. Specifications of the program:
   1. Use a Customer class to store the customer data.  This class should include these attributes: ID, firstName, lastName, company, address, city, state, zip.
   2. In addition, this class should include a property or method that returns the full address. This address should have three lines if the company attribute is empty or four lines if the company attribute is not empty.
   3. Create a function that reads the customer data from a CSV file and creates Customer objects from it.
   4. To find the customer with the specified ID, you need to loop through each Customer object in the list of Customer objects and check whether the specified ID matches the ID stored in the Customer object.
   5. If the specified ID isn’t found, display an appropriate message.
   6. You have been provided with the starter code, make sure you complete the activity and use the same function names as provided in the starter code. Also, make sure that to pass the return value from the functions wherever necessary.
   7. Push all the files into the GitHub repository.
   8. Before pushing the code to GitHub you can check to test whether your code passes all the Testcases provided in the TestActivity8.py file.
   
 ```Python
 import csv
 
 class Customer:
 
	def __init__():
		pass

def display_title():
    pass

def csv_reader():
	pass
	
def find_customer(cust_id):
	csv_reader()
	pass

def main():
	display_title()
	while True:
		cust_id = input("Enter Customer ID:")
		find_customer(cust_id)
		
		
if __name__ == '__main__':
    main()
 
 
 
 
 
 ```
		

## Submitting your assignment
1. When you are happy with your working code push the code to GitHub and be sure your GitHub repository is updated.
2. Create a markdown file/document and make one or more screenshots of the code working running in Pycharm or in the console and show successful ID numbers entered and the resulting addresses printed. Also show what happens with an ID that is not in the file. Add it to the markdown file/document labeled 4900_Activity8.

## Rubric

| Items | Exemplary  (90% - 100%) | Competent  (80% - 89%) | Acceptable  (70% - 79%) | Insufficient  (below 70%) |
|:--------------------------:|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------:|
| Python Code | Functions as described above and has appropriate comments in the code | Generally functions as described above and has some but not all comments | Partially functions as described above and may lack appropriate comments | Does not function as described above and lacks comments |
|  |  |  |  |  |
