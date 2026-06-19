import random
from datetime import date

def generate_id(): 
      id = random.randint(1000,9999)
      return id

def generate_date(): 
      today = date.today()
      return today