class NotesView:
    def __init__(self, presenter):
        self.presenter = presenter

    def create_note_view(self, title, body):

        note = self.presenter.create_note(title, body)
        print(f'Note created with ID {note.id}')

    def get_notes_view(self, date):
        if date:
            notes = self.presenter.get_notes(date)
        else:
            notes = self.presenter.get_notes()
        if notes:
            print('\n'.join([
                f"{note.id}. Title: {note.title}\n   Body: {note.body}\n   Created at: {note.created_at}\n   Updated at: {note.updated_at}"
                for note in notes
            ]))
        else:
            print('No notes found')

    def get_note_by_id_view(self, note_id):
        note = self.presenter.get_note_by_id(note_id)
        if note:
            print(note)
        else:
            print('Note not found')

    def update_note_by_id_view(self, note_id, title, body):
        note = self.presenter.update_note_by_id(note_id, title, body)
        if note:
            print(f'Note with ID {note.id} updated')

    def delete_note_by_id_view(self, note_id):
        note = self.presenter.delete_note_by_id(note_id)
        if note:
            print(f'Note with ID {note.id} deleted')
