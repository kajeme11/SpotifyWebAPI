from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secrete = os.getenv("CLIENT_SECRET")


print(client_id, client_secrete)