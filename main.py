import webbrowser, time
url = input("Enter url: ")
duration = input("Enter duration: ")
for i in range(30):
    webbrowser.open_new(url)
    time.sleep(int(duration))