import csv
import json

class DataManager:
    def __init__(self, vocabulary_file, progress_file):
        self.vocabulary_file = vocabulary_file
        self.progress_file = progress_file

    def load_vocabulary(self):
        with open(self.vocabulary_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def load_progress(self):
        try:
            with open(self.progress_file, mode='r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Trả về một dict rỗng nếu file không tồn tại hoặc không hợp lệ
            return {}

    def save_progress(self, progress):
        with open(self.progress_file, mode='w', encoding='utf-8') as file:
            json.dump(progress, file, indent=4)
            
    def update_progress(self, word):
        progress = self.load_progress()
        if word not in progress:
            progress[word] = 1
        else:
            progress[word] += 1
        self.save_progress(progress)

