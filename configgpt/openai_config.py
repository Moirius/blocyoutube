import os

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - optional dependency

    def load_dotenv(*_, **__):
        pass


try:
    from openai import OpenAI
except Exception:  # pragma: no cover - optional dependency
    OpenAI = None

# Charger la clé API depuis .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key and OpenAI:
    client = OpenAI(api_key=api_key)
else:

    class _DummyChat:
        class completions:
            @staticmethod
            def create(*_, **__):
                class _Msg:
                    content = ""

                class _Choice:
                    message = _Msg()

                class _Response:
                    choices = [_Choice()]

                return _Response()

    client = type("Dummy", (), {"chat": _DummyChat()})
