import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print ("CreatedEvent:", event)

    def on_deleted(self, event):
        print ("DeletedEvent:", event)

    def on_moved(self, event):
        print ("MovedEvent:", event)

observer = Observer()
observer.schedule(Handler(), path='/Users/Pacific/AppData/Roaming/.minecraft', recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()