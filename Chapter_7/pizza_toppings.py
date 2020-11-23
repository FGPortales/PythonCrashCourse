band = True
while(band):
    message = input("Toppin:").lower()
    if message == 'quit':
        band = False
    else:
        print(f"You have added: {message}")
