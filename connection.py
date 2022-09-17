import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '5a44ba4b-74a4-4584-bfb2-e17888e2022e'
SCPOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
   'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = r'C:\Users\PC\Pictures\hoho.jpg'
file_name = os.path.basename(file_path)
file_id = '849791C474ABC1E3'

response = requests.put(
     GRAPH_API_ENDPOINT + '/me/drives/items/' + file_id +':/'+ file_name+ ':/createUploadSession',
     headers = hearders,
     data = media_content
)
print(response.json())