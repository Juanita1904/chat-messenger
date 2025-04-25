from main import app, db, Message

with app.app_context():
    # Buscar mensajes con ID del 3 al 9
    #messages_to_delete = Message.query.filter(Message.id >= 3, Message.id <= 9).all()
    messages_to_delete = Message.query.filter(Message.user == "maria").all()

    for message in messages_to_delete:
        db.session.delete(message)
    
    db.session.commit()
    print(f"{len(messages_to_delete)} mensajes eliminados.")
