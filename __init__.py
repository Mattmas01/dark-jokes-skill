from mycroft import MycroftSkill, intent_file_handler


class DarkJokes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jokes.dark.intent')
    def handle_jokes_dark(self, message):
        self.speak_dialog('jokes.dark')


def create_skill():
    return DarkJokes()

