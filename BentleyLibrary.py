import requests
import datetime
import time
import mysql.connector
import os
from PIL import Image
import io
from Credentials import db_config
from prettytable import PrettyTable

def main():
  mydb = mysql.connector.connect(**db_config)
  
  name = ""
  lastname = ""
  email = ""
  year = 00
  ISBN = ""
  checkoutPeriod = 14
  inInventory = False
  execute = False
  newavailable_quantity = 0
  id = 0

  # Create a cursor object
  cursor = mydb.cursor()

  def list_to_string(lst):
      if len(lst) == 1:
          return str(lst[0])
      else:
          return ', '.join(map(str, lst))

  def getTitle(ISBN):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
    data = response.json()
    title = data["items"][0]["volumeInfo"]["title"]
    return title

  def getAuthor(ISBN):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
    data = response.json()
    author = data["items"][0]["volumeInfo"]["authors"]
    authorString = list_to_string(author)
    return authorString

  def getPub(ISBN):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
    data = response.json()
    pub = data["items"][0]["volumeInfo"]["publisher"]
    return pub

  def getPubDate(ISBN):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
    data = response.json()
    pub_date_str = data["items"][0]["volumeInfo"]["publishedDate"]
    
    # Attempt to parse the publication date string
    try:
      pub_date = datetime.datetime.strptime(pub_date_str, '%Y-%m-%d').date()
    except ValueError:
      # If parsing fails, use a default date of 1900-01-01
      pub_date = datetime.date(1900, 1, 1)
    
    return str(pub_date)

  def getThumbnail(ISBN):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
    data = response.json()
    thumbnail = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    return thumbnail

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
          Ans = input(Ans).lower()
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
    print("Hello. Welcome to Bentley's Libary Check In and Check Out System!")
    
    name = input("What is your first name?\n").lower()
    
    while not validString(name):
      name = input("What is your first name?\n").lower()
      print(name)
      
    lastname = input("What is your last name?\n").lower()
    
    while not validString(lastname):
        lastname = input("What is your last name?\n").lower()
        print(lastname)
    
    year = "20" + input("What year do you graduate? Please enter your year in the two digit format. Ex. 25\n")
    while True:
      if year.isalpha():
        print("You should not have letters in your year.")
      elif len(year) != 4:
        print("Year should be two numbers.")
      else: break
      year = "20" + input("What year do you graduate? Please enter your year in the two digit format. Ex. 25\n")

    email = name[0] + lastname + year[2:] + "@bentleyschool.org"
    print(f"Is this you email: {email}? ")#If yes, enter y. If no, enter n.")
    emailPrompt = "What is your email?"
    email = validyn(email, emailPrompt)
    print("fixed" + email)
    os.system("clear")
    return name.capitalize(), lastname.capitalize(), email, year

  def cico():
    global inInventory, ISBN, newavailable_quantity, id
    nonlocal execute
    name, lastname, email, year = "pat", "liu", "pliu25@bentleyschool.org", "2025" #login()
    name = name.capitalize()
    lastname = lastname.capitalize()
    print(f"Welcome {name}!")
    
    while True:
      
      ISBN = input("Please find and enter the ISBN of the book on the back cover, near the barcode. ")
      while True:
        try: 
          print(f"Is '{getTitle(ISBN)}' the book? ")
          try:
            response = requests.get(getThumbnail(ISBN))
            img = Image.open(io.BytesIO(response.content))
            img.show()
            time.sleep(2)
            img.close()
          
          except:
            pass
          
          ISBN = validyn(ISBN, "Please enter the ISBN. ")
          
          break
        except:
          print("Invalid ISBN. ")
          ISBN = input("Please enter the ISBN. ")
        
      getaval = "SELECT id, quantity, available_quantity FROM bookinventory WHERE isbn = %s"
      cursor.execute(getaval, (ISBN,))
      quanitiyResult = cursor.fetchone()
      cursor.fetchall()
      
      if not quanitiyResult:
        print("Book not found in inventory.")
        inInventory = False
      else:
        inInventory = True
        id, quantity, newavailable_quantity = quanitiyResult
      
      # Prompt the user to enter their name and action (check-in or check-out)
      if inInventory:
        
        while True:
          action = input("\nWould you like to check in or check out a book? Enter ci for check in and co for check out. Enter q to quit. ").lower()

          if action == "ci":
            # get current date as string
            current_date = datetime.date.today().strftime('%Y-%m-%d')

            # get current time as string
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            
            returned = "UPDATE log SET returned_date = %s, returned_time = %s WHERE borrower_email = %s AND isbn = %s AND returned_date IS NULL AND returned_time IS NULL ORDER BY borrowed_date DESC, borrowed_time DESC LIMIT 1"
            returnedvals = (current_date, current_time, email, ISBN)
            
            try:
              cursor.execute(returned, returnedvals)
              newavailable_quantity += 1
              if newavailable_quantity > quantity:
                newavailable_quantity = quantity
              print(f"{name} has checked in {getTitle(ISBN)} at {current_time}.")
              print("Thank you for checking in a book. Please place the book into the bin. ")
              execute = True
            except mysql.connector.Error as error:
              print("Error occurred while updating log:", error)
                
          elif action == "co":
            if newavailable_quantity > 0:
              newavailable_quantity -= 1
            else:
              print("No copies available to check out")
              continue

            # get current date as string
            current_date = datetime.date.today().strftime('%Y-%m-%d')

            # get current time as string
            current_time = datetime.datetime.now().strftime('%H:%M:%S')

            borrow = "INSERT INTO log (book_id, title, author, publisher, publication_date, isbn, borrower_first_name, borrower_last_name, borrower_email, borrowed_date, borrowed_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            borrowValues = (
            id, getTitle(ISBN), getAuthor(ISBN), getPub(ISBN), getPubDate(ISBN), ISBN, name, lastname, email,
            current_date, current_time)

            try:
              cursor.execute(borrow, borrowValues)
              print(f"{name} has checked out {getTitle(ISBN)} at {current_time}")
              print("Thank you for checking out a book.")
              execute = True
            except mysql.connector.Error as error:
              print("Error occurred while inserting into log:", error)
              
          # If the user enters an invalid action, prompt them to try again
          else:
            if action == "q":
              return
            print("Invalid action. Please enter 'ci' or 'co'.")
            # Prompt the user if they want to continue or exit the program
            exit_choice = input("Do you want to exit? Enter 'y' or 'n'. ").lower()
            if exit_choice == "y":
              return
      # Prompt the user if they want to continue or exit the program
      exit_choice = input("Do you want to exit? Enter 'y' or 'n'. ").lower()
      if exit_choice == "y":
        return

  def search(sStr):
    cursor.execute("SELECT title, author, isbn, published_date, publisher, available_quantity FROM bookinventory WHERE description LIKE %s OR author LIKE %s OR title LIKE %s OR publisher LIKE %s", ('%' + sStr + '%', '%' + sStr + '%', '%' + sStr + '%', '%' + sStr + '%'))
    results = cursor.fetchall()
    table = PrettyTable(['Title', 'Author', 'ISBN', 'Published Date', 'Publisher', 'Available Quantity'])
      
    # Add rows to the table
    for row in results:
        table.add_row(row)
    
    # Print the table
    print(table)
    input("Press Enter to continue.")
    main()  


  os.system('clear')
  menu = input("Please select from the following options.\n\n1. Search \n2. Check In & Check out\n3. Quit\n")
  if menu == "1":
    os.system('clear')
    search(input("What would you like to search for?\n"))
  elif menu == "2":
    os.system('clear')
    cico()
  elif menu == "3":
    os.system('clear')
    print("\nThank you for coming! Please contact Patrick if you have any questions.")
    time.sleep(20)
    os.system('clear')
  else:
    print("Invalid option")
    main()
    
  if execute:
    try:
      update = "UPDATE bookinventory SET available_quantity = %s WHERE id = %s"
      cursor.execute(update, (newavailable_quantity, id))
      print("Book inventory quantity updated successfully.")
      mydb.commit()
    except mysql.connector.Error as error:
      print("Error occurred while updating bookinventory:", error)

  def printall(table):
    # Execute the SELECT query
    query = "SELECT * FROM %s"
    cursor.execute(query, (table,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
      print(row)
      
main()