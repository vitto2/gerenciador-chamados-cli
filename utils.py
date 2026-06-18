import uuid
from datetime import date

def generate_id(): 
      id = str(uuid.uuid4())
      return id


def generate_date(): 
      today = date.today()
      return today