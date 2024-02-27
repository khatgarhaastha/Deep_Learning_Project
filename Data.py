import lightning as pl

from torch.utils.data import DataLoader

from aim.torch.data import val_transforms
from aim.torch.models import AIMForImageClassification
class DataModule(pl.LightningDataModule):

    def __init__(self, batch_size = 32, data_dir: str = './data', num_labels: int = 2, model_name = 'apple/aim-1B'):
        super().__init__()
        self.model_name = model_name
        self.batch_size = batch_size
        self.num_labels = num_labels
        self.data_dir = data_dir
        self.transformer = val_transforms()


    def prepare_data(self):
        '''
        Called Once per Initialization
        '''

    def transformation(self, example):
        return self.transformer(example).unsqueeze(0)

    def setup(self, stage=None):
        self.train_dataset = self.train_dataset.map(self.transformation, batched=True)
        self.val_dataset = None
        self.test_dataset = None


    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=32, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=32, shuffle=False)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=32, shuffle=False)
