from src.data_manager import DataManager

class User:
    def __init__(self, name):
        self.name = name
        self.progress = DataManager.load_progress()
        if self.name not in self.progress:
            self.progress[self.name] = {'words_learned': {}, 'score': 0}

    def update_progress(self, word, is_correct):
        """Cập nhật tiến độ học từ"""
        if word not in self.progress[self.name]['words_learned']:
            self.progress[self.name]['words_learned'][word] = 0
        if is_correct:
            self.progress[self.name]['words_learned'][word] += 1

    def get_progress(self):
        """Lấy tiến độ hiện tại"""
        return self.progress[self.name]

    def save_progress(self):
        """Lưu tiến độ người dùng"""
        DataManager.save_progress(self.progress)

