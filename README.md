# Zoom Get List Recording and Downloader

This project provides a Python script to download Zoom recordings within a specified date range. It utilizes the Zoom API to list and download recordings for a user.

## Features

- Obtain an access token using OAuth 2.0.
- List all recordings for a specified user.
- Filter recordings by date.
- Download recordings to a specified folder.

## Prerequisites

- Python 3.x
- Zoom Account with required API permissions
- Zoom OAuth App credentials (Account ID, Client ID, Client Secret)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/koswara-dev/zoom-to-youtube.git
    cd zoom-to-youtube
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of your project with your Zoom OAuth app credentials:
    ```dotenv
    ACCOUNT_ID=your_account_id_here
    CLIENT_ID=your_client_id_here
    CLIENT_SECRET=your_client_secret_here
    ```

4. Replace placeholders in the `.env` file with your actual credentials.

## Usage

To use the script, follow these steps:

1. Edit the script to configure the date range and download folder:

    ```python
    # Example usage:
    # Replace these variables with your desired date range
    start_date = '2024-06-01'  # YYYY-MM-DD
    end_date = '2024-06-15'    # YYYY-MM-DD
    download_folder = './zoom_recordings'

    # Download recordings within the specified date range
    download_recordings_by_date(ACCOUNT_ID, CLIENT_ID, CLIENT_SECRET, start_date, end_date, download_folder)
    ```

2. Run the script:
    ```bash
    python app_zoom.py
    ```

    Replace `app_zoom.py` with the actual name of your script file.

## Troubleshooting

- Make sure your Zoom OAuth App is set up correctly and that you have the necessary permissions.
- Verify the credentials in your `.env` file and make sure they are correct.
- Check your internet connection if you encounter network-related errors.

# YouTube Video Uploader

This project provides a Python script to upload videos to YouTube using a client secrets JSON file. It leverages the YouTube Data API v3 to authenticate and perform video uploads.

## Features

- Authenticate via OAuth 2.0 using client secrets.
- Upload videos to YouTube.
- Customize video metadata such as title, description, tags, and category.

## Prerequisites

- Python 3.x
- Google Cloud Platform project with YouTube Data API v3 enabled
- OAuth 2.0 Client ID JSON file from Google Cloud Console

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/koswara-dev/zoom-to-youtube.git
    cd zoom-to-youtube
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the OAuth 2.0 Client ID JSON file from the Google Cloud Console and save it in the root directory of your project as `client_secrets.json`.

4. Set up OAuth 2.0 credentials:
    Replace `YOUR_CLIENT_SECRETS_FILE` in the code with the path to your `client_secrets.json` file.

## Usage

To use the script, follow these steps:

1. Edit the script to configure the video details:
    ```python
    # Example usage:
    
    # Path to the client secrets JSON file
    CLIENT_SECRETS_FILE = "client_secrets.json"

    # Add redirect_uris in file client_secrets.json
    "redirect_uris": [
      "http://localhost:34082/"
    ]
    
    # Video settings
    VIDEO_FILE = "path_to_your_video.mp4"
    TITLE = "Video Title"
    DESCRIPTION = "Video Description"
    TAGS = ["tag1", "tag2"]
    CATEGORY = "22"  # Category ID (e.g., 22 is People & Blogs)
    ```

2. Run the script:
    ```bash
    python app_youtube.py
    ```

    Replace `app_youtube.py` with the actual name of your script file.

    On the first run, the script will prompt you to authorize access to your YouTube account. Follow the instructions to complete the authentication process.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

- Ensure that the YouTube Data API v3 is enabled for your Google Cloud project.
- Verify that the `client_secrets.json` file is correctly placed in the root directory.
- Check if all required fields in the video settings are correctly configured.

## Buy me a coffe

If you like this project and want to support its further development, buy me a coffee!

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg)](https://www.buymeacoffee.com/kudajengke404)
