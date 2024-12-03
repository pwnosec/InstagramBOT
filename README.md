
## Descriptions
An automation bot for Instagram that uploads photos from a specified directory to your Instagram account continuously. This bot processes images, ensuring they meet Instagram’s format requirements (JPEG, 1080x1080px), and posts them with customizable captions. It runs in a loop, uploading a large batch of images to Instagram while handling various error cases, including challenges, to ensure smooth operation.
This repository contains a Python script that automates the process of uploading images to Instagram. It uses the `instabot` package for interacting with Instagram's API and `PIL` for image processing. The bot is designed to continuously upload images from a local folder, ensuring they are resized to the appropriate dimensions and format for Instagram. It handles challenges and errors during the login and uploading process, making it suitable for long-running automation tasks.

### Features:
 - Logs into Instagram automatically.
 - Processes images to meet Instagram's photo requirements.
 - Handles transparency in PNGs by adding a white background.
 - Uploads photos continuously, with a configurable delay between uploads.
 - Capable of running for extended periods, uploading multiple images (up to 1000 or more).
 - Handles errors such as challenge-required and upload failures.



### Requirements:
 - Python `3.x`
 - `instabot` library
 - `Pillow` for image processing




> [!NOTE]
> This project is still under active development, and exciting new features will be added in the coming months. Stay tuned for more advanced capabilities to be released in 2025! Keep an eye on this repository to see the latest updates and improvements.






