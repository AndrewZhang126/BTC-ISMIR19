from audio_dataset import AudioDataset
from utils.mir_eval_modules import audio_file_to_features
from utils.hparams import HParams
import matplotlib.pyplot as plt
from torch import optim



# Plan: use AudioDataLoader to load audio data
# 
# Use CQT to transofrm them into spectrograms
# 
# Train an autoencoder w/ normalization to convert to hypersphere representationz
#
# Create a forward function that ends at the feature layer to use in loss function
# 
config = HParams.load("run_config.yaml")

audio_path = 'input_data/Beatles/Audio/Lovely Rita.mp3'
feature, feature_per_second, song_length_second = audio_file_to_features(audio_path, config)

train_dataset1 = AudioDataset(config, root_dir=config.path['root_path'], dataset_names=("Beatles",), num_workers=20, preprocessing=False, train=True, kfold=1)


print(feature.shape, feature_per_second, song_length_second)
