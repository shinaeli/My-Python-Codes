def send_messages(messages):
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    print(sent_messages)


message_list = ['How are you?', 'How was your day?', 'Have a great day.']

send_messages(message_list)

print(message_list)