from src.vocabulary import Vocabulary
from src.user import User
from src.ui_manager import UIManager

class App:
    def __init__(self):
        self.user = User(name="Default User")
        self.vocabulary = Vocabulary()
        self.ui_manager = UIManager()

    def start_app(self):
        """Khởi chạy ứng dụng"""
        print("Welcome to the English Learning App!")
        topics = self.vocabulary.get_topics()
        self.ui_manager.display_topics(topics, self.show_topic_vocab)

    def show_topic_vocab(self, topic):
        """Hiển thị từ vựng theo chủ đề"""
        words = self.vocabulary.get_words_by_topic(topic)
        for word in words:
            print(f"{word['word']} ({word['meaning']})")  # Hoặc sử dụng UI để hiển thị
            self.ui_manager.display_vocab(word['word'], word['image_path'])

