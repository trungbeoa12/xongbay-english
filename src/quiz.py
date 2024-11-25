import random

class Quiz:
    def __init__(self, vocabulary):
        """
        Khởi tạo quiz với danh sách từ vựng.
        :param vocabulary: Danh sách từ vựng (dạng dictionary).
        """
        self.vocabulary = vocabulary

    def generate_question(self):
        """
        Tạo câu hỏi kiểm tra từ vựng.
        :return: Từ đúng (correct_word), danh sách lựa chọn (choices).
        """
        correct_word = random.choice(self.vocabulary)  # Chọn từ đúng ngẫu nhiên
        
        # Đảm bảo số lựa chọn không vượt quá số từ trong danh sách
        num_choices = min(4, len(self.vocabulary))  # Tối đa 4 lựa chọn (bao gồm từ đúng)
        choices = random.sample(self.vocabulary, num_choices - 1)  # Chọn các từ sai
        
        # Đảm bảo từ đúng nằm trong danh sách lựa chọn
        if correct_word not in choices:
            choices.append(correct_word)
        
        random.shuffle(choices)  # Xáo trộn danh sách lựa chọn
        return correct_word, choices

