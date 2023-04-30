import json
import datetime


class Note:
    def __init__(self, id, title, body, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

    def __str__(self):
        return f'ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.isoformat() if hasattr(self.created_at, 'isoformat') else self.created_at,
            'updated_at': self.updated_at.isoformat() if hasattr(self.updated_at, 'isoformat') else self.updated_at
        }


class NotesModel:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as f:
                notes = [Note(**note) for note in json.load(f)]
        except FileNotFoundError:
            notes = []
        return notes

    def save_notes(self):
        with open(self.filename, 'w') as f:
            json.dump([note.to_dict() for note in self.notes], f)

    def get_notes(self, date=None):
        if date:
            date = datetime.datetime.fromisoformat(date).date()
            notes = [note for note in self.notes if datetime.datetime.fromisoformat(note.created_at).date() == date]
        else:
            notes = self.notes

        # сортировка заметок по дате создания, начиная с только что созданных
        return sorted(notes, key=lambda note: note.created_at, reverse=True)


    def create_note(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)
        self.save_notes()
        return note

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)

    def update_note_by_id(self, note_id, title=None, body=None):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title or note.title
            note.body = body or note.body
            note.updated_at = datetime.datetime.now()
            self.save_notes()
            return note

    def delete_note_by_id(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            return note