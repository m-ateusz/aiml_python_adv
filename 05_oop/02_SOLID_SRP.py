class Report:
   def __init__(self, data: list[dict]):
       self.data = data

class ReportFormatter:
   @staticmethod
   def generate_text(report: Report) -> str:
       lines = ["REPORT"]
       for row in report.data:
           lines.append(f"- {row['name']}: {row['value']}")
       return "\n".join(lines)

class FileWriter:
   def save_to(self, text: str, uri: str) -> None:
       with open(uri, "w", encoding="utf-8") as f:
           f.write(text)

class JsonFileWriter(FileWriter):
    def save_to(self, text: str, uri: str) -> None:
        ...

class LogWriter:
   def save_to(self, text: str, uri) -> None:
       pass

report = Report([{'name': 'mateusz', 'value': '10$'}, {'name': 'alice', 'value': '-10$'}])
text = ReportFormatter.generate_text(report)
print(f'{text}')