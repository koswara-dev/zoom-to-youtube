import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCOUNT_ID = os.getenv('ACCOUNT_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_access_token(account_id, client_id, client_secret):
    # Endpoint for getting an access token
    token_url = 'https://zoom.us/oauth/token'
    
    payload = {
        'grant_type': 'account_credentials',
        'account_id': account_id
    }
    
    # Basic authentication with client id and client secret
    response = requests.post(token_url, params=payload, auth=(client_id, client_secret))
    
    if response.status_code != 200:
        raise Exception("Failed to obtain access token: {0}".format(response.text))

    return response.json()['access_token']

def get_all_recordings(account_id, client_id, client_secret):
    access_token = get_access_token(account_id, client_id, client_secret)
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    base_url = 'https://api.zoom.us/v2/users/me/recordings'
    recordings = []
    
    next_page_token = ''
    while True:
        params = {
            'page_size': 30,
            'next_page_token': next_page_token
        }
        
        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise Exception("Failed to retrieve recordings: {0}".format(response.text))
        
        data = response.json()
        recordings.extend(data.get('meetings', []))
        
        next_page_token = data.get('next_page_token', '')
        if not next_page_token:
            break
    
    return recordings

def filter_recordings_by_date(recordings, start_date, end_date):
    filtered_recordings = [rec for rec in recordings if start_date <= rec['start_time'][:10] <= end_date]
    return filtered_recordings

def download_recording(recording_url, download_path):
    response = requests.get(recording_url, stream=True)
    if response.status_code == 200:
        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print(f"Failed to download recording. Status code: {response.status_code}")

def download_recordings_by_date(account_id, client_id, client_secret, start_date, end_date, download_folder):
    all_recordings = get_all_recordings(account_id, client_id, client_secret)
    filtered_recordings = filter_recordings_by_date(all_recordings, start_date, end_date)
    
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for recording in filtered_recordings:
        for file in recording['recording_files']:
            download_url = file['download_url'] + "?access_token=" + get_access_token(account_id, client_id, client_secret)
            file_name = f"{recording['id']}_{file['id']}.mp4"
            download_path = os.path.join(download_folder, file_name)
            print(f"Downloading {file_name}...")
            download_recording(download_url, download_path)
            print(f"Downloaded {file_name} to {download_path}")

# Example usage:
# Replace these variables with your desired date range
start_date = '2024-07-18'  # YYYY-MM-DD
end_date = '2024-07-18'    # YYYY-MM-DD
download_folder = './zoom_recordings'

# Download recordings within the specified date range
download_recordings_by_date(ACCOUNT_ID, CLIENT_ID, CLIENT_SECRET, start_date, end_date, download_folder)
