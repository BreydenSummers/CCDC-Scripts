from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class SimpleChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_modified(self, event):
        print(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")


def watch_folders(paths):
    event_handler = SimpleChangeHandler()
    observer = Observer()
    for path in paths:
        observer.schedule(event_handler, path, recursive=True)
        print(f"Watching folder: {path}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped watching folders")

    observer.join()


if __name__ == "__main__":
    folders_to_watch = [
        "./downloads",
        "./projects",
        "/etc/sysctl.conf",
        "/etc/security/limits.conf",
        "/etc/syslog.conf",
        "/etc/network/interfaces",
        "/etc/resolv.conf",
        "/etc/passwd",
        "/etc/group",
        "/etc/shadow",
        "/etc/fstab",
        "/etc/mtab",
    ]
    watch_folders(folders_to_watch)

