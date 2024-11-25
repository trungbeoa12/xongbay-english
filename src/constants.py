import os

# Đường dẫn cơ sở của dự án
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Đường dẫn đến các thư mục và file
DATA_DIR = os.path.join(BASE_DIR, 'data')
AUDIO_DIR = os.path.join(DATA_DIR, 'audio')
IMAGES_DIR = os.path.join(DATA_DIR, 'images')
VOCAB_FILE = os.path.join(DATA_DIR, 'vocabulary.csv')
PROGRESS_FILE = os.path.join(DATA_DIR, 'progress.json')

# Cấu hình cấp độ
LEVELS = {
    1: "Beginner",
    2: "Intermediate",
    3: "Advanced"
}

