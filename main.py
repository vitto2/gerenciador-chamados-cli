import tickets

def show_menu():
    print("=== Ticket System ===")
    print("1 - Open ticket")
    print("2 - List tickets")
    print("3 - Search ticket by ID")
    print("4 - Update status")
    print("0 - Exit\n")


def main():     
    while True: 
        show_menu()
        option = input("Choose a option:")
        match option:
          case "1":
                tickets.open_ticket()
          case "2": 
                tickets.show_tickets()
          case "0": 
           break
    

if __name__ == "__main__":
    main()