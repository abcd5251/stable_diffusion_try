import gdown
import os 

url_checkpoint = "https://drive.google.com/u/3/uc?id=1eWGYAmcxw4-MyZwrgFg640SuhVKNnLSb&export=download"
url_vae = "https://drive.google.com/u/3/uc?id=1PbbkksgXckaD0vvKFExGqLEr3I3pzPst&export=download"
url_easyNegative =  "https://drive.google.com/u/3/uc?id=1QLjlbIMHxtMqkZH4mnok5GITrJg4Uv6Q&export=download"

checkp oint_saveplace = "./stable-diffusion-webui/models/Stable-diffusion/Counterfeit-V2.5.safetensors"
vae_saveplace = "./stable-diffusion-webui/models/VAE/Counterfeit-V2.5.vae.pt"
easyNegative_saveplace = "./stable-diffusion-webui/embeddings/EasyNegative.safetensors"

gdown.download(url_checkpoint, checkpoint_saveplace)
gdown.download(url_vae, vae_saveplace)
gdown.download(url_easyNegative, easyNegative_saveplace)