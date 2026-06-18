import database
import utils

def open_ticket(): 
  title = input("Title: ")
  desc = input("Describe your ticket: ")
  applicant = input("your name: ")
  priorit = input("priorit: ")
  
  print("Ticket registered\n\n")

  ticket = { 
    "title": title, 
    "describe": desc, 
    "Applicant": applicant, 
    "Priorit": priorit,
    "id": utils.generate_id(),
    "date": utils.generate_date(),
    "status": "Open"
  }

  database.tickets.append(ticket)


def show_tickets():
    print(database.tickets)