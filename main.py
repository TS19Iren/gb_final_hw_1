from model import NotesModel
from presenter import NotesPresenter
from view import NotesView
from arg_parser import ArgumentParser

argument_parser = ArgumentParser()
args = argument_parser.parse_args()

model = NotesModel('notes.json')
presenter = NotesPresenter(model)
view = NotesView(presenter)

if args.command == 'add':
    view.create_note_view(args.title, args.body)
elif args.command == 'read':
    if args.id:
        view.get_note_by_id_view(args.id)
    elif args.date:
        view.get_notes_view(args.date)
    else:
        view.get_notes_view(args.date)
elif args.command == 'update':
    view.update_note_by_id_view(args.id, args.title, args.body)
elif args.command == 'delete':
    view.delete_note_by_id_view(args.id)
