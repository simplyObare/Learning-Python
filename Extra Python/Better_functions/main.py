from datetime import datetime

def get_time() -> str:
   """
   this is a function that gets current time in the users locale and returns it as a string
   
   Example:   
   >>>> get_time()
   "01:27:52"
   """
   
   
   now: datetime = datetime.now()
   return f"{now:%X}"

print(get_time())