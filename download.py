import gdown
import os 

# choose whether checkpoint or icon 
url_checkpoint = "https://drive.google.com/u/3/uc?id=1eWGYAmcxw4-MyZwrgFg640SuhVKNnLSb&export=download"
url_vae = "https://drive.google.com/u/3/uc?id=1PbbkksgXckaD0vvKFExGqLEr3I3pzPst&export=download"
url_easyNegative =  "https://drive.google.com/u/3/uc?id=1QLjlbIMHxtMqkZH4mnok5GITrJg4Uv6Q&export=download"
#url_icon_checkpoint = "https://drive.google.com/u/3/uc?id=1O6n1YN6DOA0MV2702T6KIusgWBAUteiz&export=download"



checkpoint_saveplace = "./models/Stable-diffusion/Counterfeit-V2.5.safetensors"
vae_saveplace = "./models/VAE/Counterfeit-V2.5.vae.pt"
easyNegative_saveplace = "./embeddings/EasyNegative.safetensors"

gdown.download(url_icon_checkpoint, checkpoint_saveplace)
gdown.download(url_vae, vae_saveplace)
gdown.download(url_easyNegative, easyNegative_saveplace)