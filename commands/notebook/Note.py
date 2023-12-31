from classes.notebook.Notebook import Notebook
from classes.notebook.RecordNote import RecordNote
from helpers.decorators import input_error

class NoteCommands:

    @input_error
    def add_note_title(args, book: Notebook):
        note_name, note_text, note_tags = args
        note = book.find(note_name)
        if note:
            return "Note already exists"
        record = RecordNote(note_name)
        record.add_note(note_text)
        record.add_tag(note_tags)
        book.add_record(record)
        return "Note entry created."


    @input_error
    def remove_note(args, book: Notebook):
        note = book.find(args[0])
        if note:
            book.delete(args[0])
            return "Note deleted successfully."
        else:
            return "Note not found."