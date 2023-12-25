import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QProgressBar, QFileDialog

api_key = 'YOUR_GOOGLE_API_KEY'

def search_google_images(query, start, count):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": "YOUR_CUSTOM_SEARCH_ENGINE_ID",
        "searchType": "image",
        "q": query,
        "start": start,
        "num": count
    }
    response = requests.get(url, params=params)
    return response.json()

# Function to download images
def download_images(image_urls, folder_path, progress_bar):
    total_images = len(image_urls)
    progress_step = 100 / total_images if total_images > 0 else 0
    progress_value = 0

    for idx, image_url in enumerate(image_urls):
        try:
            response = requests.get(image_url)
            with open(f"{folder_path}/image_{idx+1}.jpg", "wb") as file:
                file.write(response.content)
        except Exception as e:
            print(f"Download failed: {e}")

        progress_value += progress_step
        progress_bar.setValue(int(progress_value))

    progress_bar.setValue(100)

class ImageDownloader(QWidget):
    # ... (Rest of the code remains the same)

    def start_download(self):
        count = self.entry_count.text()
        query = self.entry_query.text()
        folder_path = self.entry_folder.text()
        max_count = 30
        count = min(max_count, int(count)) if count.isdigit() else 1
        os.makedirs(folder_path, exist_ok=True)

        self.progress_bar.setValue(0)

        start_idx = 1
        while start_idx <= count:
            results = search_google_images(query, start_idx, count)
            image_urls = [item['link'] for item in results.get('items', [])]

            download_images(image_urls, folder_path, self.progress_bar)
            start_idx += len(image_urls)

            if len(image_urls) < count:
                break

        QMessageBox.information(self, "Complete", "Image download completed!")

    # ... (Rest of the code remains the same)
