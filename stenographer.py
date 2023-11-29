import csv
# import os
import datetime
import re

class Stenographer:
    def __init__(self, shorthand_file):
        self.shorthand_file = shorthand_file
        self.load_shorthand_expansions()
        self.notes_buffer = []

    def load_shorthand_expansions(self):
        self.expansions = {}
        with open(self.shorthand_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)  # Debug print
                self.expansions[row[0]] = row[1]

    def expand_notes(self, note):
        for shorthand, expansion in self.expansions.items():
            note = re.sub(r'\b' + re.escape(shorthand) + r'\b', expansion, note)
        priority_pattern = r'-\d+'
        matches = re.findall(priority_pattern, note)
        for match in matches:
            priority_tag = f"[Priority: {match[1:]}]"
            note = note.replace(match, priority_tag)
        return note

    def format_notes(self):
        formatted_notes = {"Attendees": [],"Key Takeaways": [], "Action Items": [], "Notes": [], "Research Items": []}
        for note in self.notes_buffer:
            if "@" in note:
                formatted_notes["Attendees"].append(note.replace("@", ""))
            elif "!" in note:
                formatted_notes["Action Items"].append(note.replace("!", ""))
            elif "#" in note:
                formatted_notes["Key Takeaways"].append(note.replace("#", ""))
            elif "-?" in note:
                formatted_notes["Research Items"].append(note.replace("-?", ""))
            else:
                formatted_notes["Notes"].append(note)
        return formatted_notes

    def save_notes(self, formatted_notes):
        filename = f"./notes/Stenographer_Notes_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(filename, "w") as file:
            for section, notes in formatted_notes.items():
                if len(notes) > 0:
                    file.write(f"{section}:\n")
                for note in notes:
                    file.write(f"- {note.lstrip()}\n")
                file.write("\n")

    def run(self):
        print("""\n
----------------------------------------------------------------------------
Stenographer is running. Type your notes and press Enter.
Press Ctrl+C to save and exit.
              
Markdown tags (descending order of priority - only one tag per line)      
| Attendees: @        
| Action Item: !
| Key Takeaway: #
| Research Item: -?
              
Item Priority: -1, -2, -3, etc...(Can append to any line in addition to tag)
----------------------------------------------------------------------------
""")
        try:
            while True:
                try:
                    note = input()
                    expanded_note = self.expand_notes(note)
                    self.notes_buffer.append(expanded_note)
                except KeyboardInterrupt:
                    break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received, ending session...")
        finally:
            formatted_notes = self.format_notes()
            self.save_notes(formatted_notes)
            print("Notes saved successfully.")

stenographer = Stenographer("library.csv")
stenographer.run()
