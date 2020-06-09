from flask import Blueprint, jsonify, request
from . import db
# from .models import Movie
from .models import Note

main= Blueprint('main',__name__)


# Add a Note
@main.route('/add_note', methods=['POST'])
def add_note():
    note_data = request.get_json()

    new_note = Note(title=note_data['title'], content=note_data['content'])

    db.session.add(new_note)
    db.session.commit()

    return 'Done', 201

#Show Notes
@main.route('/notes')
def notes():
    note_list = Note.query.all()
    notes = []

    for note in note_list:
        notes.append({'title': note.title, "content": note.content})

    return jsonify({'notes': notes})



#Update Note
# @main.route('/product<id>', methods=['PUT'])
# def update_note(id):
#     note = Note.query.get(id)

#     title = request.json['title']
#     content = request.json['content']

#     note.title = title
#     note.content = content
    
#     db.session.commit()

#     return jsonify({'notes':notes})



# #Delete a Note
# @app.route('/delete/<id>'methods=['DELETE'])
# def delete_note(id):
#     note = Note.query.get(id)
#     db.session(note)
#     db.session.commit()