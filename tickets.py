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
    "applicant": applicant,
    "priorit": priorit,
    "id": utils.generate_id(),
    "date": utils.generate_date(),
    "status": "Open"
  }

  database.tickets.append(ticket)


def show_tickets():
    tickets = database.tickets
    if len(tickets) == 0:
        print("Não há chamados registrados no momento.\n")
    else:
         for ticket in database.tickets:
            print(
                f"\nID: {ticket['id']}\n"
                f"Title: {ticket['title']}\n"
                f"Describe: {ticket['describe']}\n"
                f"Applicant: {ticket['applicant']}\n"
                f"Priority: {ticket['priorit']}\n"
                f"Date: {ticket['date']}\n"
                f"Status: {ticket['status']}\n\n"
            )



def search_tickets():
   tickets = database.tickets
   id = input("\nInsira o ID do ticket: ")

   ticket = [ticket for ticket in tickets if ticket["id"] == id]
   print(f"{ticket}")