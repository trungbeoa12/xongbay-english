from src.data_manager import DataManager

class Vocabulary:
    def __init__(self):
        self.words = DataManager.load_vocabulary()

    def get_word(self, word):
        """Tìm một từ cụ thể"""
        for w in self.words:
            if w['word'] == word:
                return w
        return None

    def get_words_by_level(self, level):
        """Lấy danh sách từ theo cấp độ"""
        return [w for w in self.words if int(w['level']) == level]

    def get_words_by_topic(self, topic):
        """Lấy danh sách từ theo chủ đề"""
        return [w for w in self.words if w['topic'].lower() == topic.lower()]   

    def get_topics(self):
        """Lấy danh sách tất cả các chủ đề"""
        return list(set(w['topic'] for w in self.words))

