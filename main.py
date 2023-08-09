from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import datetime
import random


class LogInScreen(Screen):
    def __init__(self, **kwargs):
        super(LogInScreen, self).__init__(**kwargs)

        # Set the background color using RGB (0, 71, 54)
        Window.clearcolor = (0, 0.28, 0.21, 1)
        # Create widgets
        layout = BoxLayout(orientation='vertical', spacing='20dp', padding='50dp')
        # Set background color using RGB (0, 71, 54)
        # with layout.canvas.before:
        # Color(1,1,1,1)
        # self.rect = Rectangle(pos=layout.pos, size=layout.size)

        logo_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        logo = Image(source='jhs.png', size_hint=(1, 1), allow_stretch=False, keep_ratio=True)
        # logo_label = Label(size_hint=(0.8, 1))
        logo_layout.add_widget(logo)
        # logo_layout.add_widget(logo_label)
        title_label = Label(text='Welcome to QuizApp!', font_size='30sp', color=(1, 1, 1, 1))

        self.username_input = TextInput(multiline=False, hint_text="Enter your username",
                                        size_hint_y=None, height='40dp',
                                        background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                                        foreground_color=(0, 0, 0, 1))
        self.password_input = TextInput(multiline=False, password=True, hint_text="Enter your password",
                                        size_hint_y=None, height='40dp',
                                        background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                                        foreground_color=(0, 0, 0, 1))
        login_button = Button(text="Log In", size_hint_y=None, height='40dp',
                              background_normal='', background_color=(0.1, 0.4, 0.5, 0.7),
                              color=(1, 1, 1, 1))
        login_button.bind(on_press=self.check_login)
        # Add widgets to layout
        layout.add_widget(logo_layout)
        layout.add_widget(title_label)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        # Set the layout as the LoginScreen's root widget
        self.add_widget(layout)

    def check_login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text
        # Perform credential validation (hardcoded for simplicity)
        if username == "user" and password == "password":
            quiz_app.username = username
            quiz_app.screen_manager.current = "quiz_screen"
        else:
            self.show_popup()

    def show_popup(self):
        content = BoxLayout(orientation='vertical', spacing='10dp')
        popup_label = Label(text="Invalid username or password!", font_size='18sp',
                            color=(1, 0, 0, 1), size_hint_y=None, height='30dp', halign='center')
        ok_button = Button(text="OK", size_hint_y=None, height='40dp', on_press=self.dismiss_popup)

        content.add_widget(popup_label)
        content.add_widget(ok_button)

        popup = Popup(title="Warning", content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def dismiss_popup(self, instance):
        instance.parent.parent.parent.parent.dismiss()


class QuizScreen(Screen):
    questions = [
        {
            "question": "a. What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "b. Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "c. What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "1. What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "2. Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "3. What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "What is the capital of France?/What is the capital of France?/What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
            "correct_answer": "Blue Whale"
        }
    ]

    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.current_question = 0
        self.score = 0

        self.question_label = Label(text="", font_size=18, size_hint_y=None,
                                    halign='center', valign='middle', markup=True,
                                    text_size=(800, None))
        self.options_buttons = []
        for i in range(4):  # Assuming each question has 4 options, adjust this number accordingly
            button = Button(text="", on_press=self.check_answer, size_hint_y=None, height='40dp',
                            background_normal='', background_color=(0.1, 0.4, 0.5, 0.7))
            self.options_buttons.append(button)

        layout = BoxLayout(orientation="vertical", spacing='20dp', padding='50dp')
        layout.add_widget(self.question_label)
        for button in self.options_buttons:
            layout.add_widget(button)

        self.add_widget(layout)
        self.show_question()
        self.selected_answers = []  # Create a list to store the selected answers

    def on_enter(self, *args):
        self.show_question()

    def shuffle_questions(self):
        # Shuffle the questions list
        random.shuffle(self.questions)

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            # Shuffle the questions before displaying
            self.shuffle_questions()
            question_data = self.questions[self.current_question]

            # Shuffle the options for the current question
            options = question_data["options"]
            random.shuffle(options)

            self.question_label.text = question_data["question"]
            for i, button in enumerate(self.options_buttons):
                button.text = options[i]

        else:
            self.save_answers()
            quiz_app.screen_manager.current = "result_screen"

    def check_answer(self, instance):
        question_data = self.questions[self.current_question]
        selected_answer = instance.text
        if selected_answer == question_data["correct_answer"]:
            self.score += 1

        # Store the selected answer for the current question
        self.selected_answers.append(selected_answer)

        self.current_question += 1
        self.show_question()

    def save_answers(self):
        filename = "quiz_answers.txt"
        with open(filename, "w") as file:
            file.write(f"Username: {quiz_app.username}\n")
            file.write(
                f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {quiz_app.quiz_screen.score}/{len(quiz_app.quiz_screen.questions)}\n")
            for i, question_data in enumerate(self.questions):
                selected_answer = self.selected_answers[i] if i < len(self.selected_answers) else "No answer"
                file.write(f"{i + 1} {selected_answer}")  # f"Item Number: {i + 1}\n")
                # file.write(f" {selected_answer}\n") #Selected Answer: {selected_answer}\n")
                file.write("\n")


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.score_label = Label(text="", font_size=20)
        self.save_button = Button(text="Save Answers", on_press=self.save_answers_to_file, size_hint_y=None,
                                  height='40dp',
                                  background_normal='', background_color=(0.1, 0.4, 0.5, 0.7))

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Congratulations! Quiz is completed.", size_hint_y=None,
                                halign='center', valign='middle', markup=True,
                                text_size=(800, None)))
        layout.add_widget(self.score_label)
        layout.add_widget(self.save_button)  # Add the save button to the layout
        self.add_widget(layout)

    def on_enter(self, *args):
        self.score_label.text = f"Your score: {quiz_app.quiz_screen.score}/{len(quiz_app.quiz_screen.questions)}"

    def save_answers_to_file(self, instance):
        quiz_app.quiz_screen.save_answers()
        # After saving the answers, change the screen back to the quiz screen
        # quiz_app.screen_manager.current = "quiz_screen"


class SirAbbyQuizApp(App):
    username = ""

    def build(self):
        self.screen_manager = ScreenManager()

        self.log_in_screen = LogInScreen(name="log_in_screen")
        self.quiz_screen = QuizScreen(name="quiz_screen")
        self.result_screen = ResultScreen(name="result_screen")

        self.screen_manager.add_widget(self.log_in_screen)
        self.screen_manager.add_widget(self.quiz_screen)
        self.screen_manager.add_widget(self.result_screen)

        return self.screen_manager


if __name__ == "__main__":
    quiz_app = SirAbbyQuizApp()
    quiz_app.run()
