import json
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class FeedbackEntry:
    id: str
    prompt: str
    response_a: str
    response_b: str
    preferred: str

class FeedbackCollector:
    def __init__(self, path: str = "data/feedback.jsonl"):
        self.path = path
    
    def collect(self, entry: FeedbackEntry):
        with open(self.path, 'a') as f:
            f.write(json.dumps(asdict(entry)) + '\n')