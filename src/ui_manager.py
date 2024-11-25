import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pygame


class UIManager:
    def __init__(self, image_dir, audio_manager, quiz):
        self.image_dir = image_dir
        self.audio_manager = audio_manager
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("English Learning for Kids")
        self.window.geometry("800x600")  # Đặt kích thước cửa sổ
        self.window.resizable(False, False)  # Không cho phép thay đổi kích thước
        self.window.config(bg="#f0f8ff")  # Màu nền xanh nhạt
        self.current_index = 0
        self.words = []
        self.score = 0
        self.total_questions = 0

        # Tạo menu
        self.create_menu()

        # Tạo frame chính
        self.main_frame = tk.Frame(self.window, bg="#f0f8ff")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo label hiển thị điểm
        self.score_label = tk.Label(
            self.window, text="Score: 0", font=("Comic Sans MS", 16), fg="blue", bg="#f0f8ff"
        )
        self.score_label.pack(side=tk.TOP, pady=5)

        # Khởi tạo pygame mixer
        pygame.mixer.init()

    def create_menu(self):
        menu_bar = tk.Menu(self.window)

        # Menu "File"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.window.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Menu "Modes"
        mode_menu = tk.Menu(menu_bar, tearoff=0)
        mode_menu.add_command(label="Learning Mode", command=self.display_word)
        mode_menu.add_command(label="Quiz Mode", command=self.start_quiz)
        menu_bar.add_cascade(label="Modes", menu=mode_menu)

        # Menu "Help"
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.window.config(menu=menu_bar)

    def show_about(self):
        messagebox.showinfo("About", "English Learning for Kids\nVersion 1.0")

    def load_words(self, words):
        self.words = words

    def clear_main_frame(self):
        # Xóa tất cả widget trong frame chính
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def display_word(self):
        self.clear_main_frame()

        if not self.words:
            return
        word = self.words[self.current_index]["word"]

        # Hiển thị từ
        label = tk.Label(self.main_frame, text=word, font=("Arial", 24), bg="#f0f8ff")
        label.pack()

        # Hiển thị hình ảnh
        image_file = os.path.join(self.image_dir, f"{word}.jpg")
        if os.path.exists(image_file):
            image = Image.open(image_file)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            label_image = tk.Label(self.main_frame, image=photo, bg="#f0f8ff")
            label_image.image = photo
            label_image.pack()

        # Nút chuyển từ
        btn_next = tk.Button(self.main_frame, text="Next", command=self.next_word)
        btn_next.pack(side=tk.RIGHT, padx=10)

        btn_prev = tk.Button(self.main_frame, text="Previous", command=self.prev_word)
        btn_prev.pack(side=tk.LEFT, padx=10)

        # Phát âm thanh
        self.audio_manager.play_audio(word)

    def next_word(self):
        if self.current_index < len(self.words) - 1:
            self.current_index += 1
            self.display_word()

    def prev_word(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_word()

    def start_quiz(self):
        """
        Bắt đầu chế độ kiểm tra. Reset điểm và hiển thị câu hỏi đầu tiên.
        """
        self.clear_main_frame()
        self.score = 0
        self.total_questions = len(self.words)
        self.score_label.config(text="Score: 0")  # Reset điểm

        # Thêm thanh tiến trình
        self.progress = ttk.Progressbar(self.window, length=400, mode='determinate')
        self.progress.pack(pady=10)
        self.progress["value"] = 0  # Reset tiến trình
        self.progress["maximum"] = len(self.words)

        # Thông báo bắt đầu
        messagebox.showinfo("Start Quiz", f"Bắt đầu bài kiểm tra!\nTổng số câu hỏi: {self.total_questions}")
        self.next_question()

    def next_question(self):
        """
        Hiển thị câu hỏi tiếp theo.
        """
        self.clear_main_frame()

        if self.total_questions > 0:
            correct_word, choices = self.quiz.generate_question()

            # Hiển thị hình ảnh
            image_file = os.path.join(self.image_dir, f"{correct_word['word']}.jpg")
            if os.path.exists(image_file):
                image = Image.open(image_file)
                image = image.resize((200, 200))
                photo = ImageTk.PhotoImage(image)
                label_image = tk.Label(self.main_frame, image=photo, bg="#f0f8ff")
                label_image.image = photo
                label_image.grid(row=0, column=0, columnspan=2, pady=20)

            # Hiển thị các nút lựa chọn
            for i, choice in enumerate(choices):
                btn_choice = tk.Button(
                    self.main_frame,
                    text=choice['word'],
                    font=("Comic Sans MS", 16),
                    bg="#add8e6",
                    activebackground="#87cefa",
                    command=lambda c=choice: self.check_answer(correct_word, c)
                )
                btn_choice.grid(row=i + 1, column=0, padx=20, pady=5)

            # Nút "Back"
            btn_back = tk.Button(
                self.main_frame,
                text="Back",
                font=("Comic Sans MS", 14),
                bg="#ffcccb",
                command=self.display_word
            )
            btn_back.grid(row=len(choices) + 1, column=0, columnspan=2, pady=10)

    def check_answer(self, correct_word, chosen_word):
        """
        Kiểm tra câu trả lời của người dùng.
        """
        if correct_word == chosen_word:
            self.play_sound("data/sounds/correct.mp3")
            messagebox.showinfo("Correct", f"Bạn đã trả lời đúng! Đáp án là: {correct_word['word']}.")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")  # Cập nhật điểm
        else:
            self.play_sound("data/sounds/incorrect.mp3")
            messagebox.showerror("Incorrect", f"Sai rồi! Đáp án đúng là: {correct_word['word']}.")

        self.total_questions -= 1
        self.progress["value"] += 1  # Cập nhật tiến trình

        if self.total_questions > 0:
            self.next_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        """
        Hiển thị điểm cuối cùng khi hoàn thành bài kiểm tra.
        """
        result = messagebox.askyesno(
            "Quiz Completed",
            f"Bạn đã hoàn thành bài kiểm tra!\nĐiểm số của bạn: {self.score}/{len(self.words)}\nBạn có muốn chơi lại không?"
        )
        if result:
            self.start_quiz()
        else:
            self.display_word()

    def play_sound(self, sound_file):
        """
        Phát âm thanh từ tệp.
        """
        if os.path.exists(sound_file):
            pygame.mixer.music.stop()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

    def run(self):
        self.display_word()
        self.window.mainloop()

