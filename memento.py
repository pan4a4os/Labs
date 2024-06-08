class Snapshot:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content

class Document:
    def __init__(self):
        self._content = ""

    def set_content(self, content):
        print(f"Setting content: {content}")
        self._content = content

    def get_content(self):
        return self._content

    def save_to_snapshot(self):
        print("Saving content to Snapshot")
        return Snapshot(self._content)

    def restore_from_snapshot(self, snapshot):
        self._content = snapshot.get_content()
        print(f"Restoring content from Snapshot: {self._content}")

class Editor:
    def __init__(self):
        self._snapshots = []

    def add_snapshot(self, snapshot):
        self._snapshots.append(snapshot)

    def get_snapshot(self, index):
        return self._snapshots[index]

document = Document()
editor = Editor()

document.set_content("Version 1")
editor.add_snapshot(document.save_to_snapshot())

document.set_content("Version 2")
editor.add_snapshot(document.save_to_snapshot())

document.set_content("Version 3")
editor.add_snapshot(document.save_to_snapshot())

document.restore_from_snapshot(editor.get_snapshot(1))
document.restore_from_snapshot(editor.get_snapshot(0))
