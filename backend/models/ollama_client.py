# Import relevant libraries

import requests
import json

# Define the base URL for handling the requests. 

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

# Function to chat with Elrond the fat one

def ask_elrond(prompt):
    payload = {
        "model" : "phi3:3.8b-q4-k-m",
        "messages" : [
            {"role" : "user"}, 
            {"content" : prompt}
        ]
    }
    
    