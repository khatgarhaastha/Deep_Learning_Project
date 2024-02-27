import lightning as pl
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class Model(pl.LightningModule):

    def __init__(self, model_name = ''):
        super().__init__()
        pass

    def forward(self, x):
        pass

    def training_step(self, batch, batch_idx):
        pass

    def validation_step(self, batch, batch_idx):
        pass

    def test_step(self, batch, batch_idx):
        pass

    def configure_optimizers(self):
        pass

