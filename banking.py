def main():
  print("Program start")

  file_transactions_name = "transactions.txt"
  file_customer_name = "customer.txt"

  transactions_file = open (file_transactions_name, "r")
  customer_file = open (file_customer_name, "r")  

  customers = []
  transactions = []

  transactions_read = transactions_file.readline()
  customer_read = customer_file.readline()

  while customer_read != "":

    customer_read = customer_read.strip("\n")
    customer_read = customer_read.split()
    customers.append(customer_read)
    customer_read = customer_file.readline()

  while transactions_read != "":

    transactions_read = transactions_read.strip("\n")
    transactions_read = transactions_read.split()
    transactions.append(transactions_read)
    transactions_read = transactions_file.readline()
  stop_question =input ("Enter Y to continue. Enter N to quit: ")

  while stop_question!= "N":
    id_question = int(input("Enter your customer ID: "))
  
  
    display_question = int(input("Would you like to display the current summary or history of transactions? \nEnter 1 for summary. \nEnter 2 for history : "))
  
    for i in customers:
      if int(i[0]) == id_question:
        current_balance = 0
        if  display_question == 1:
  
          print("The current summary for ID", i[0], "is \nFirst Name:", i[1], "\nLast Name:", i[2], "\nSingle or Family:", i[3], "\nOwns Home?", i[4])
          for j in transactions:
            if int(j[0]) == id_question:
              if j[2] == "C":
                current_balance += float(j[3])
  
              elif j[2] == "D":
                current_balance -= float(j[3])
  
  
        elif display_question == 2:
          print("The original balance was: $", current_balance)
          for j in transactions:
            if int(j[0]) == id_question:
              if j[2] == "C":
                current_balance += float(j[3])
                print("Sequence number: ", j[1], "\nAfter the credit of", j[3], "The current balance is: $", current_balance)
              elif j[2] == "D":
                current_balance -= float(j[3])
                print("Sequence number: ", j[1], "\nAfter the debit of", j[3], "The current balance is: $", current_balance)
        print("The current balance is: $", current_balance)
    stop_question =input ("Enter Y to continue. Enter N to quit: ")
  else: 
    print("Quitted")
  
  
          #After processing one line, get the next from the file
  
  
  transactions_file.close()
  customer_file.close()

  print("Program done")
########################

main()

input()
