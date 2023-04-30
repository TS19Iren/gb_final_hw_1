class NotesPresenter:
    def __init__(self, model):
        self.model = model

    def create_note(self, title, body):
        return self.model.create_note(title, body)

    def get_notes(self, date=None):
        return self.model.get_notes(date)

    def get_note_by_id(self, note_id):
        return self.model.get_note_by_id(note_id)

    def update_note_by_id(self, note_id, title=None, body=None):
        return self.model.update_note_by_id(note_id, title, body)

    def delete_note_by_id(self, note_id):
        return self.model.delete_note_by_id(note_id)