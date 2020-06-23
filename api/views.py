from flask import Blueprint, jsonify, request
from . import db
from .models import Note

main = Blueprint('main', __name__)


# Add a Note
@main.route('/add_note', methods=['POST'])
def add_note():
    note_data = request.get_json()

    new_note = Note(title=note_data['title'], content=note_data['content'])

    db.session.add(new_note)
    db.session.commit()

    return 'Done', 201

# Show Notes
@main.route('/notes')
def notes():
    note_list = Note.query.all()
    notes = []

    for note in note_list:
        notes.append({'id': note.id, 'title': note.title,
                      "content": note.content})

    return jsonify({'notes': notes})


@main.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    return 'deleted'


@main.route('/add_note/<id>', methods=['PUT'])
def update(id):
    note = Note.query.get(id)

    title = request.json['title']
    content = request.json['content']

    note.title = title
    note.content = content

    db.session.commit()

    return 'updated'
