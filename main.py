from src.data_manager import DataManager
from src.audio_manager import AudioManager
from src.ui_manager import UIManager
from src.quiz import Quiz

def main():
    vocabulary_file = "data/vocabulary.csv"
    progress_file = "data/progress.json"
    audio_dir = "data/audio"
    image_dir = "data/images"

    # Initialize managers
    data_manager = DataManager(vocabulary_file, progress_file)
    audio_manager = AudioManager(audio_dir)
    vocabulary = data_manager.load_vocabulary()

    # Initialize Quiz
    quiz = Quiz(vocabulary)

    # Initialize UI
    ui_manager = UIManager(image_dir, audio_manager, quiz)  # Truyền quiz trực tiếp vào UIManager
    ui_manager.load_words(vocabulary)

    # Run UI
    ui_manager.run()

if __name__ == "__main__":
    main()


