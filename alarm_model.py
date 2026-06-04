from dataclasses import dataclass, field
import uuid

@dataclass
class Alarm:
    time: str
    label: str
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    active: bool = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "time": self.time,
            "label": self.label,
            "active": self.active
        }

    @staticmethod
    def from_dict(data: dict) -> "Alarm":
        return Alarm(
            id=data["id"],
            time=data["time"],
            label=data["label"],
            active=data["active"]
        )