import requests
from config import API_KEY

def v1_search(endpoint):
    r = requests.get(f"https://cryven.biz/api/v1/search/{endpoint}&key={API_KEY}")
    data = r.json()
    return data

def main():
   value = input("""[0] Search\n\n->> """)
   if value == "0":
     phone = input("[0] Send phone number (example: 77779997777)\n\n->> ")
     time = input("[1] Send time (example: fast, advanced)\n\n->> ")
     data = v1_search(f"?phone={phone}&time={time}")
     print(data)
   else:
      print("We don't understand this request.")

main()
