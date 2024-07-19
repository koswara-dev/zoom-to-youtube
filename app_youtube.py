import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the scopes required by your application
SCOPES = ['https://www.googleapis.com/auth/youtube.upload', 'https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    """Get authenticated service."""
    creds = None
    
    # Token file stores the user's access and refresh tokens
    token_path = 'token.pickle'
    
    # Delete token.pickle file if exists to force re-authentication
    if os.path.exists(token_path):
        os.remove(token_path)
        print("Previous token.pickle deleted. Re-authenticate with the correct scopes.")
    
    # If no credentials are found, or the credentials are invalid/incomplete, request new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh the credentials
            creds.refresh(Request())
        else:
            # Run local server flow to get credentials
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=34082)
        
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    
    return build('youtube', 'v3', credentials=creds)

# Function to fetch channel info
def fetch_channel_info(service):
    request = service.channels().list(
        part='snippet',
        mine=True
    )
    response = request.execute()
    print(response)

# Function to upload video to YouTube
def upload_video(service, video_file_path, title, description, category_id, privacy_status):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': privacy_status  # "public", "private" or "unlisted"
        }
    }
    
    media_body = MediaFileUpload(video_file_path, chunksize=-1, resumable=True)
    
    request = service.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media_body
    )
    
    response = request.execute()
    print(response)
    
def main():
    # Get the authenticated service
    youtube_service = get_authenticated_service()

    while True:
        print("\nSelect an action:")
        print("1. Fetch Channel Info")
        print("2. Upload Video")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            fetch_channel_info(youtube_service)
        elif choice == '2':
            video_file_path = input("Enter the path to your video file: ")
            title = input("Enter the video title: ")
            description = input("Enter the video description: ")
            category_id = input("Enter the category ID (e.g., 22 for 'People & Blogs'): ")
            privacy_status = input("Enter the privacy status (public/private/unlisted): ")
            upload_video(youtube_service, video_file_path, title, description, category_id, privacy_status)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
