class ModerationClient:

    def check(self, text: str):
        if not text.strip():
            return {"allowed": False, "flag": "empty_input"}

        lowered = text.lower()

        if "kill" in lowered or "hate" in lowered:
            return {"allowed": False, "flag": "violence_or_hate"}

        return {"allowed": True}