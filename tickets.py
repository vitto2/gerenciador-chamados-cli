import database

def open_ticket(): 
  title = input("Title: ")
  desc = input("Describe your ticket: ")
  applicant = input("your name: ")
  priorit = input("priorit: ")

  print("Ticket registered")

  ticket = { 
    "title": title, 
    "describe": desc, 
    "Applicant": applicant, 
    "Priorit": priorit
  }

  database.tickets.append(ticket)


def show_tickets():
    print(database.tickets)