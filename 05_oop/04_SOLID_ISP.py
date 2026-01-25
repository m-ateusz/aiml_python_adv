from typing import Protocol, runtime_checkable

class EmailSender(Protocol):
   def send_email(self, to: str, subject: str, body: str) -> None: ...

class SmsSender(Protocol):
   def send_sms(self, phone: str, text: str) -> None: ...

class PushSender(Protocol):
   def send_push(self, user_id: str, title: str, body: str) -> None: ...


class SmtpEmailSender:
   def send_email(self, to: str, subject: str, body: str) -> None:
       print(f"EMAIL to={to} subject={subject}")


class MobileNotifier:
    def send_sms(self, phone: str, text: str) -> None:
        print(f"SMS to={phone} text={text}")

    def send_push(self, user_id: str, title: str, body: str) -> None:
        print(f"push to={user_id} title={title} body={body}")


class FloodNotifier:
    def send_email(self, to: str, subject: str, body: str) -> None:
        print(f"FLOOD NOTIFIER to={to} subject={subject}")

    def send_sms(self, phone: str, text: str) -> None:
        print(f"SMS to={phone} text={text}")

    def send_push(self, user_id: str, title: str, body: str) -> None:
        print(f"push to={user_id} title={title} body={body}")

def notify_by_email(notifier: EmailSender) -> None:
    notifier.send_email("recipient", "subject", 'body')


notify_by_email(SmtpEmailSender())



