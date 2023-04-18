import requests
import datetime
import time
import mysql.connector
import os
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

#Credentials

#test
# host = os.environ.get('DB_HOST')

# if host is None:
#     print("Environment variable 'host' is not set.")
# else:
#     print("Environment variable 'host' is set to:", host)

mydb = mysql.connector.connect(
  host=os.getenv('DB_HOST'),
  user=os.getenv('DB_USER'),
  password=os.getenv('DB_PASSWORD'),
  database=os.getenv('DB_NAME'),
)

name = ""
lastname = ""
email = ""
year = 00
checkoutPeriod = 14

# Get the current time
current_time = datetime.datetime.now()

# Format the current date as a string
current_time_str = current_time.strftime('%Y-%m-%d')

# Add the checkout period to the current datetime object
due_date = current_time + datetime.timedelta(days=checkoutPeriod)

# Format the due date as a string
due_date_str = due_date.strftime('%Y-%m-%d')

# Create a cursor object
cursor = mydb.cursor()

# Prepare the SQL query to insert data
mycursor = mydb.cursor()

# Insert data into the table
sql = "INSERT INTO yourtable (Title, Author, Publication_Date, ISBN, User_First_Name, User_Last_Name, User_Email, User_Grad_Year, Number_of_Current_Book_Checked_Out, Due_Date, Status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

def getTitle(ISBN):
  response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
  data = response.json()
  title = data["items"][0]["volumeInfo"]["title"]
  return title

def getAuthor(ISBN):
  response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
  data = response.json()
  author = data["items"][0]["volumeInfo"]["authors"]
  authorString = ', '.join(author)
  return authorString

def getPubDate(ISBN):
  response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
  data = response.json()
  date = data["items"][0]["volumeInfo"]["publishedDate"]
  return date

def getThumbnail(ISBN):
  response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
  data = response.json()
  date = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
  return date

def validyn(var, prompt):
  while True:
    
    Ans = input(f"Is this correct? (y/n) ").lower()
    if Ans == "n":
      var = input(prompt)
    elif Ans == "y":
      return var
    else:
      print("Invalid Entry")
      while Ans != "y" or Ans != "n":
        Ans = input(str).lower()
        if Ans == "n":
          var = input(prompt)
        elif Ans == "y":
          return var

def validString(str):
  if not str.isalpha():
    # print(not str.isaplha(), str)
    print("Please enter letters only.")
    return False
  elif len(str) <= 1:
    print("Name must be more that one letter")
    return False
  return True

def login():
  print("Hello. Welcome to Bentley's Libary Check In and Check Out System! Press Enter/Return to Continue.")
  
  name = input("What is your first name?\n").lower()
  
  while not validString(name):
    name = input("What is your first name?\n").lower()
    print(name)
    
  lastname = input("What is your last name?\n").lower()
  
  while not validString(lastname):
      lastname = input("What is your last name?\n").lower()
      print(lastname)
  
  year = input("What year do you graduate? Please enter your year in the two digit format. Ex. 25\n")
  while True:
    if year.isalpha():
      print("You should not have letters in your year.")
    elif len(year) != 2:
      print("Year should be two numbers.")
    else: break
    year = input("What year do you graduate? Please enter your year in the two digit format. Ex. 25\n")

  email = name[0] + lastname + year + "@bentleyschool.org"
  print(f"Is you email: {email}? ")#If yes, enter y. If no, enter n.")
  emailPrompt = "What is your email?"
  validyn(email, emailPrompt)
  print("fixed" + email)
  os.system("clear")
  return name, lastname, email, year

def main():
  
  name, lastname, email, year = login()
  print(f"Welcome {name}!")
  
  while True:
    # Prompt the user to enter their name and action (check-in or check-out)
    action = input("Would you like to check in or check out a book? Enter ci for check in and co for check out. ")



    # If the user is checking in, add their name and check-in time to the dictionary
    if action == "ci":
      
      
      ISBN = input("Please find and enter the ISBN of the book on the back cover, near the barcode. ")
      while True:
        try: 
      
          print(f"Is '{getTitle(ISBN)}' the book you are checking in? If yes, enter y. If no, enter n. ")
          response = requests.get(getThumbnail(ISBN))
          img = Image.open(io.BytesIO(response.content))
          img.show()
          time.sleep(2)
          img.close()
          validyn(ISBN, "Please enter the ISBN. ")
          break
        except:
          print("Invalid ISBN. ")
          ISBN = input("Please enter the ISBN. ")

      value = (getTitle(ISBN), getAuthor(ISBN), getPubDate(ISBN), ISBN, name, lastname, email, year, "1", current_time_str, "Checked In")
      
      mycursor.execute(sql, value)
          
      # check_in_out = {"name": name, "ISBN": ISBN, "check-in": current_time}
      # db[name] = check_in_out
      # print(db[name])
      # print(f"{name} has checked in {getTitle(ISBN)} at {current_time}")
      print(f"{name} has checked out {getTitle(ISBN)} at {current_time}")
      print("Thank you for checking out a book.")
    # If the user is checking out, add their check-out time to the dictionary
    elif action == "co":
        # Check if the user has checked in before
        ISBN = input("Please find and enter the ISBN of the book on the back cover, near the barcode. ")
        while True:
          try: 
            print(f"Is '{getTitle(ISBN)}' the book you are checking out? ")
            
            validyn(ISBN, "Please enter the ISBN. ")
            response = requests.get(getThumbnail(ISBN))
            img = Image.open(io.BytesIO(response.content))
            img.show()
            time.sleep(2)
            img.close()
            break
          except:
            print("Invalid ISBN. ")
            ISBN = input("Please enter the ISBN. ")

        
        value = (getTitle(ISBN), getAuthor(ISBN), getPubDate(ISBN), ISBN, name, lastname, email, year, "1", due_date_str, "Checked Out")
        for v in value:
          print(v)
          print(type(v))

        mycursor.execute(sql, value)    
        #val = ("The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10", 9780684830421, "John", "Doe", "johndoe@gmail.com", 2023, 1, "2023-05-01")
        print(f"{name} has checked out {getTitle(ISBN)} at {current_time}")
        print("Thank you for checking out a book.")
    # If the user enters an invalid action, prompt them to try again
    else:
        print("Invalid action. Please enter 'ci' or 'co'.")

    # Prompt the user if they want to continue or exit the program
    exit_choice = input("Do you want to exit? Enter 'y' or 'n'. ").lower()
    if exit_choice == "y":
      break

main()

# Commit the changes to the database
mydb.commit()

# Close the connection
print(mycursor.rowcount, "record inserted.")
mydb.close()

def printall():
  # Execute the SELECT query
  mycursor.execute("SELECT * FROM new_table")

  # Fetch all rows from the result set
  rows = mycursor.fetchall()

  # Print each row
  for row in rows:
    print(row)