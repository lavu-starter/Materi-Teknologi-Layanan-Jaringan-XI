def chatbot():
    print("=== Chatbot Helpdesk Jaringan ===")
    while True:
        user = input("Anda: ").lower()
        if "ip" in user:
            print("Bot: IP bisa dicek dengan perintah ipconfig (Windows) atau ifconfig (Linux).")
        elif "dns" in user:
            print("Bot: DNS menerjemahkan nama domain menjadi alamat IP.")
        elif "proxy" in user:
            print("Bot: Proxy bertindak sebagai perantara antara user dan internet.")
        elif "exit" in user:
            print("Bot: Terima kasih sudah bertanya!")
            break
        else:
            print("Bot: Maaf, saya belum paham pertanyaan Anda.")

chatbot()
