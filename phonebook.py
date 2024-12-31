#Importing pickle library
import pickle as p
# Adding Initial Contacts to the phonebook
f=open("Phonebook.dat",'wb')
# Creating an empty dictionary
D = {}
print("-----------------------------------------------------------------------------------------")
n = int(input("Enter the number of contacts you initially want to enter:"))
print()
for i in range(1, n + 1):
   print("Contact number", i)
   name = input("Enter the Name:")
   phone = input("Enter the phone number:")
   email = input("Enter the E-Mail:")
   dob = input("Enter the Date of Birth of the person:")
   print()
   D[name] = [phone, email, dob]
print("-----------------------------------------------------------------------------------------")
print()
pickle.dump(D,f)
f.close()
# Function for displaying the contact Details
def display():
   f = open("Phonebook.dat", 'rb')
   D=p.load(f)
   lsno = []
   for i in range(1, len(D) + 1):
       lsno.append(i)
   lnme = []
   ldob = []
   lph = []
   lem = []
   for key in D:
       lph.append(D[key][0])
       lem.append(D[key][1])
       ldob.append(D[key][2])
       lnme.append(key)
   from prettytable import PrettyTable
   #Prettytable is an external Module which can be downloaded usig pip statement in the Terminal
   columns = [" S.NO", "Contact Name", "Phone number", "Email ID", "Date of Birth"]
   myTable = PrettyTable()
   myTable.add_column(columns[0],lsno)
   myTable.add_column(columns[1],lnme)
   myTable.add_column(columns[2],lph)
   myTable.add_column(columns[3],lem)
   myTable.add_column(columns[4],ldob)
   print(myTable)
   f.close()


# Function for Adding a new contact
def Addcontact():
   f = open("Phonebook.dat", 'rb')
   D = p.load(f)
   print("-----------------------------------------------------------------------------------------")
   name = input("Enter the Name of the new Contact:")
   phone = input("Enter the phone number of the new contact:")
   email = input("Enter the E-Mail of the new contact:")
   dob = input("Enter the Date of Birth of the new contact:")
   print("-----------------------------------------------------------------------------------------")
   D[name] = [phone, email, dob]
   f.close()
   f = open("Phonebook.dat", 'wb')
   p.dump(D,f)
   f.close()

def deletecontact():
   f = open("Phonebook.dat", 'rb')
   D = p.load(f)
   dl = input("Enter the name of the contact you want to delete:")
   if dl in D:
       del D[dl]
   else:
       print()
       print("The given contact name is not present in the phonebook.")
   f.close()
   f = open("Phonebook.dat", 'wb')
   p.dump(D, f)
   f.close()

# Function for editing an existing Contact
def editcon():
   f = open("Phonebook.dat", 'rb')
   D = p.load(f)
   nme = input("Enter the name of the contact you want to edit:")
   if nme in D:
       print("-----------------------------------------------------------------------------------------")
       print("------Contact editing------")
       print()
       print("1.Editing the Contact name")
       print("2.Editing Contact Details")
       print("3.Editing both the contact name and details")
       print()
       c1 = int(input("Enter your choice:"))
       print()
       if c1 == 1:
           phone = D[nme][0]
           email = D[nme][1]
           dob = D[nme][2]
           del D[nme]
           nme = input("Enter the new name:")
       elif c1 == 2:
           phone = input("Enter the new phone number:")
           email = input("Enter the new E-Mail:")
           dob = input("Enter the Date of birth of the person:")
       elif c1 == 3:
           del D[nme]
           nme = input("Enter the new name:")
           phone = input("Enter the new phone number:")
           email = input("Enter the new E-Mail:")
           dob = input("Enter the Date of birth of the person:")
       D[nme] = [phone, email, dob]
       f.close()
       f = open("Phonebook.dat", 'wb')
       p.dump(D, f)
       f.close()
       print("-----------------------------------------------------------------------------------------")
   else:
       print()
       print("The given Contact Name is not present in the Phonebook.")
       f.close()



# Function for Searching a Contact
def searchc():
   f = open("Phonebook.dat", 'rb')
   D = p.load(f)
   print("-----------------------------------------------------------------------------------------")
   print("------Searching A Contact------")
   print("1.Search A Contact on the basis of Name. ")
   print("2.Search A Contact on the basis of Phone. ")
   print("3.Search A Contact on the basis of E-Mail. ")
   print("To Go Back,Enter Any other choice.")
   print()
   cho = int(input("Enter your choice:"))
   print()
   if cho == 1:
       snm = input("Enter The Contact name you want to Search:")
       print()
       if snm in D:
           print(snm)
           print("Contact Number:", D[snm][0])
           print("Contact E-Mail ID:", D[snm][1])
           print("Date of Birth of Contact:", D[snm][2])
       else:
           print("Invalid Contact")
   elif cho == 2:
       sph = input("Enter The Phone number on basis of which you want to search the Contact:")
       print()
       check1=0
       for p in D:
           if sph == D[p][0]:
               check1=1
               print(p)
               print("Contact Number:", D[p][0])
               print("Contact E-Mail ID:", D[p][1])
               print("Date of Birth of Contact:", D[p][2])
       if check1==0:
           print("Invalid Contact")
   elif cho == 3:
       check2=0
       sem = input("Enter The E-Mail on basis of which you want to search the Contact:")
       print()
       for m in D:
           if sem == D[m][1]:
               check2=1
               print(m)
               print("Contact Number:", D[m][0])
               print("Contact E-Mail ID:", D[m][1])
               print("Date of Birth of Contact:", D[m][2])
       if check2==0:
           print("Invalid Contact")
       else:
           print("Invalid Contact")
   print("----------------------------------------------------------------------------------------------------------")
   f.close()


# Infinite While loop for Menu Based Program
while True:
   print("-------------------------Phone Book-------------------------")
   print()
   print("1.Display all contact details")
   print("2.Add a new contact")
   print("3.Delete a contact")
   print("4.Edit a contact")
   print("5.Search for a contact")
   print("Enter any other choice to exit the phonebook.")
   print()
   ch = int(input("Enter your choice:"))
   print()
   if ch == 1:
       display()
   elif ch == 2:
       Addcontact()
   elif ch == 3:
       deletecontact()
   elif ch == 4:
      editcon()
   elif ch == 5:
       searchc()
   else:
       print("Thank you for using our Phonebook.")
       print("Efforts by:-")
       print("Krish Marwah")
       print("Adyut Gupta")
       print("Arnav Anand")
       print("Goodbye!")
       break
   print()
   print()
 
