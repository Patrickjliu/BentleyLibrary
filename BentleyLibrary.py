import requests
from datetime import datetime
import os
name = ""
lastname = ""
email = ""
checkoutPeriod = 14

def getTitle(ISBN):
  response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{ISBN}")
  data = response.json()
  title = data["items"][0]["volumeInfo"]["title"]
  return title

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
    print("loop")

def validString(str):
  if not str.isalpha():
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
    
  name = input("What is your last name?\n").lower()
  
  while validString(lastname):
      name = input("What is your last name?\n").lower()
  
  year = input("What year do you graduate? Please enter your year in the two digit format. Ex. 25\n")
  while True:
    if year.isalpha():
      print("You should not have letters in your year.")
    elif len(year) != 2:
      print("Year should be two numbers.")
    else: break
    year = input("What year do you graduate? Please enter your year in the two digit format. Ex. 25\n")

  email = name[0] + lastname + year + "@bentleyschool.org"
  
  print(f"Is you email: {name[0]}{lastname}{year}@bentleyschool.org? If yes, enter y. If no, enter n.")
  emailPrompt = "What is your email?"
  validyn(email, emailPrompt)
  
  os.system("clear")
name = "Patrick"
def main():
    
  print(f"Welcome {name}!")
  
  while True:
    # Prompt the user to enter their name and action (check-in or check-out)
    action = input("Would you like to check in or check out a book? Enter ci for check in and co for check out. ")

    # Get the current time
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%d %H:%M")

    # If the user is checking in, add their name and check-in time to the dictionary
    if action == "ci":
      
      
      ISBN = input("Please find and enter the ISBN of the book on the back cover, near the barcode. ")
      while True:
        try: 
      
          print(f"Is '{getTitle(ISBN)}' the book you are checking in? If yes, enter y. If no, enter n. ")
          
          validyn(ISBN, "Please enter the ISBN. ")
          break
        except:
          print("Invalid ISBN. ")
          ISBN = input("Please enter the ISBN. ")
          
      # check_in_out = {"name": name, "ISBN": ISBN, "check-in": current_time}
      # db[name] = check_in_out
      # print(db[name])
      # print(f"{name} has checked in {getTitle(ISBN)} at {current_time}")

    # If the user is checking out, add their check-out time to the dictionary
    elif action == "co":
        # Check if the user has checked in before
        ISBN = input("Please find and enter the ISBN of the book on the back cover, near the barcode. ")
        while True:
          try: 
            print(f"Is '{getTitle(ISBN)}' the book you are checking out? If yes, enter y. If no, enter n. ")
            
            validyn(ISBN, "Please enter the ISBN. ")
            break
          except:
            print("Invalid ISBN. ")
            ISBN = input("Please enter the ISBN. ")
            
        # check_in_out = {"name": name, "ISBN": ISBN, "check-out": current_time}
        # db[name] = check_in_out
        # print(db[name])
        # print(f"{name} has checked out {getTitle(ISBN)} at {current_time}")

    # If the user enters an invalid action, prompt them to try again
    else:
        print("Invalid action. Please enter 'ci' or 'co'.")

    # Prompt the user if they want to continue or exit the program
    exit_choice = input("Do you want to exit? Enter 'y' or 'n'. ").lower
    if exit_choice == "y":
        break

login()
main() 