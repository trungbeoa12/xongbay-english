from gtts import gTTS
import os

# Danh sách từ vựng đầy đủ
words = [
    # Gia đình
    "father", "mother", "sister", "brother", "baby", 
    "grandfather", "grandmother", "uncle", "aunt", "cousin",

    # Các bộ phận cơ thể
    "head", "face", "hair", "eye", "ear", "nose", "mouth", "teeth",
    "hand", "arm", "leg", "foot", "finger", "toe", "stomach",

    # Đồ vật trong nhà
    "bed", "chair", "table", "sofa", "lamp", "door", "window", "clock", 
    "pillow", "blanket", "fridge", "cup", "plate", "spoon", "fork",

    # Đồ dùng học tập
    "book", "notebook", "pen", "pencil", "ruler", "eraser", "bag", 
    "sharpener", "glue", "scissors", "crayon", "paper", "desk", "board", "marker",

    # Màu sắc
    "red", "blue", "yellow", "green", "orange", "purple", "pink", 
    "black", "white", "brown", "gray", "gold", "silver",

    # Động vật
    "cat", "dog", "bird", "fish", "cow", "pig", "horse", "sheep", 
    "duck", "chicken", "lion", "tiger", "elephant", "monkey", "bear", 
    "snake", "rabbit", "frog", "giraffe", "zebra",

    # Số đếm
    "one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty",

    # Thời tiết
    "sun", "rain", "wind", "snow", "cloud", "rainbow", "hot", "cold", 
    "warm", "storm",

    # Thức ăn và đồ uống
    "apple", "banana", "orange", "grape", "watermelon", "mango", 
    "strawberry", "rice", "bread", "milk", "water", "juice", "tea", 
    "egg", "cheese", "chicken", "fish", "meat", "soup", "ice cream",

    # Đồ vật ngoài trời
    "tree", "flower", "grass", "stone", "sky", "star", "moon", "sun", 
    "river", "mountain", "beach", "sea", "sand",

    # Hành động
    "run", "jump", "eat", "drink", "sleep", "play", "walk", "talk", 
    "sing", "dance", "draw", "write", "read", "swim", "climb", 
    "sit", "stand", "open", "close", "watch",

    # Tính từ mô tả
    "big", "small", "tall", "short", "happy", "sad", "fast", "slow", 
    "hot", "cold", "good", "bad", "clean", "dirty", "beautiful", "ugly",

    # Quần áo
    "shirt", "pants", "dress", "skirt", "jacket", "coat", "sweater", 
    "shoes", "socks", "hat", "cap", "scarf", "gloves", "belt", "backpack",

    # Phương tiện giao thông
    "car", "bus", "train", "plane", "bicycle", "boat", "motorbike", 
    "truck", "taxi", "ship",

    # Các ngày và tháng
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", 
    "Sunday", "January", "February", "March", "April", "May", 
    "June", "July", "August", "September", "October", "November", "December",

    # Thời gian
    "morning", "afternoon", "evening", "night", "today", "tomorrow", 
    "yesterday", "hour", "minute", "second",

    # Địa điểm
    "home", "school", "park", "shop", "market", "hospital", "zoo", 
    "farm", "library", "playground",

    # Cảm xúc
    "happy", "sad", "angry", "scared", "excited", "tired", 
    "surprised", "bored", "confused"
]

# Thư mục lưu file âm thanh
output_folder = "/home/trungdt2/Thuchanh/Xongbay'senglish/code_tao_data/audio_files"
os.makedirs(output_folder, exist_ok=True)

# Tạo file âm thanh cho từng từ
for word in words:
    try:
        tts = gTTS(text=word, lang='en')
        file_path = os.path.join(output_folder, f"{word}.mp3")
        tts.save(file_path)
        print(f"Đã tạo file âm thanh: {file_path}")
    except Exception as e:
        print(f"Lỗi khi tạo file cho từ '{word}': {e}")
