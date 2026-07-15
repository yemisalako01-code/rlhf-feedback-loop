import torch
from transformers import AutoModelForSequenceClassification

class RewardModelTrainer:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=1)
    
    def train(self, preferred_scores, rejected_scores):
        loss = -torch.nn.functional.logsigmoid(preferred_scores - rejected_scores).mean()
        return loss