import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import notification

# Читаем аффирмации из файла
def get_random_affirmation():
    
    with open("affirmations.txt", "r", encoding="utf-8") as file:
        affirmations = file.readlines()
    return random.choice(affirmations).strip()

# Главный класс приложения
class AffirmationApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.button = Button(
            text="Показать аффирмацию",
            font_size=20,
            size_hint=(1, 0.2)
        )
        self.button.bind(on_press=self.show_affirmation)
        
        layout.add_widget(self.button)
        return layout

    def show_affirmation(self, instance):
        affirmation = get_random_affirmation()
        notification.notify(
            title="Твоя аффирмация дня",
            message=affirmation,
            app_name="Daily Affirmations"
        )

# Запуск приложения
if __name__ == "__main__":
    AffirmationApp().run()
