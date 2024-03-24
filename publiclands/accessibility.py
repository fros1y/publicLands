from enum import StrEnum


class Accessibility(StrEnum):
    OPEN = "Open Access"
    LIMITED = "Limited Public Access"
    CLOSED = "Closed to Public Access"
    UNKNOWN = "Unknown"

    def __str__(self):
        return self.value
