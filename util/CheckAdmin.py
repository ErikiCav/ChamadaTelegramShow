def CheckAdmin(update):
    lista_ids = ""
    for user in update.message.chat.get_administrators():
        lista_ids += f" {user.user.id}"
    if(f"{update.message.from_user.id}" in f"{lista_ids}"):
        return True
    else:
        return False

def CheckAdmin_query(update):
    lista_ids = ""
    for user in update.message.chat.get_administrators():
        lista_ids += f" {user.user.id}"
    if(f"{update.from_user.id}" in f"{lista_ids}"):
        return True
    else:
        return False