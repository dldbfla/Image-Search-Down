import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QProgressBar, QFileDialog

client_id = '네이버 api 아이디'
client_secret = '네이버 api 비번'

def search_naver_images(query, start, count):
    url = "https://openapi.naver.com/v1/search/image"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    params = {
        "query": query,
        "display": count,
        "start": start
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

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
            print(f"다운로드 실패: {e}")

        progress_value += progress_step
        progress_bar.setValue(int(progress_value))

    progress_bar.setValue(100)

class ImageDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('이미지 다운로더')
        self.setGeometry(100, 100, 400, 250)

        main_layout = QVBoxLayout()

        count_layout = QHBoxLayout()
        label_count = QLabel('다운로드할 이미지 개수를 입력하세요 (최대 30개):', self)
        count_layout.addWidget(label_count)
        self.entry_count = QLineEdit(self)
        self.entry_count.setPlaceholderText('최대 30개까지 입력 가능합니다.')
        count_layout.addWidget(self.entry_count)

        query_layout = QHBoxLayout()
        label_query = QLabel('검색할 이름을 입력하세요:', self)
        query_layout.addWidget(label_query)
        self.entry_query = QLineEdit(self)
        query_layout.addWidget(self.entry_query)

        folder_layout = QHBoxLayout()
        label_folder = QLabel('이미지를 저장할 폴더를 입력하세요:', self)
        folder_layout.addWidget(label_folder)
        self.entry_folder = QLineEdit(self)
        self.entry_folder.setReadOnly(True)
        folder_layout.addWidget(self.entry_folder)

        folder_button = QPushButton('이미지 저장 폴더 선택', self)
        folder_button.clicked.connect(self.open_folder_dialog)
        folder_layout.addWidget(folder_button)

        main_layout.addLayout(count_layout)
        main_layout.addLayout(query_layout)
        main_layout.addLayout(folder_layout)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        self.button_download = QPushButton('이미지 다운로드', self)
        self.button_download.clicked.connect(self.start_download)
        main_layout.addWidget(self.button_download)

        self.setLayout(main_layout)

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
            results = search_naver_images(query, start_idx, count)
            image_urls = [item['link'] for item in results['items']]

            download_images(image_urls, folder_path, self.progress_bar)
            start_idx += len(image_urls)

            if len(image_urls) < count:
                break

        QMessageBox.information(self, "완료", "이미지 다운로드가 완료되었습니다.")

    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, '이미지 저장 폴더 선택')
        if folder_path:
            self.entry_folder.setText(folder_path)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = ImageDownloader()
    ex.show()
    sys.exit(app.exec_())
