import sys
import os
import wget
import zipfile
from types import SimpleNamespace
from helpers.model_load import load_model, get_model_output_paths
from helpers.depth import DepthModel

from transformers import T5Tokenizer, T5EncoderModel, CLIPTokenizer, CLIPTextModel

sys.path.insert(0, "src")


def PathSetup():
    models_path = "/deforum-stable-diffusion/models"  # @param {type:"string"}
    configs_path = "configs"  # @param {type:"string"}
    output_path = "outputs"  # @param {type:"string"}
    mount_google_drive = True  # @param {type:"boolean"}
    models_path_gdrive = "/content/drive/MyDrive/AI/models"  # @param {type:"string"}
    output_path_gdrive = "/content/drive/MyDrive/AI/StableDiffusion"  # @param {type:"string"}
    return locals()


root = SimpleNamespace(**PathSetup())
root.models_path, root.output_path = get_model_output_paths(root)


def ModelSetup():
    # @param ["cpu", "cuda"]
    map_location = "cpu"

    # @param ["custom","v2-inference.yaml","v2-inference-v.yaml","v1-inference.yaml"]
    model_config = "v1-inference.yaml"

    # @param ["custom","v2-1_768-ema-pruned.ckpt","v2-1_512-ema-pruned.ckpt","768-v-ema.ckpt","512-base-ema.ckpt","Protogen_V2.2.ckpt","v1-5-pruned.ckpt","v1-5-pruned-emaonly.ckpt","sd-v1-4-full-ema.ckpt","sd-v1-4.ckpt","sd-v1-3-full-ema.ckpt","sd-v1-3.ckpt","sd-v1-2-full-ema.ckpt","sd-v1-2.ckpt","sd-v1-1-full-ema.ckpt","sd-v1-1.ckpt", "robo-diffusion-v1.ckpt","wd-v1-3-float16.ckpt"]
    model_checkpoint = "Protogen_V2.2.ckpt"

    # @param {type:"string"}
    custom_config_path = ""

    # @param {type:"string"}
    custom_checkpoint_path = ""
    return locals()


root.__dict__.update(ModelSetup())

try:
    load_model(root, load_on_run_all=True, check_sha256=True, map_location=root.map_location)
except Exception as err:
    print(err)

CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")

T5Tokenizer.from_pretrained("google/t5-v1_1-xl")
T5EncoderModel.from_pretrained("google/t5-v1_1-xl")

# Initialize DepthModel
depth_model = DepthModel(root.map_location)

# Load and cache the models
depth_model.load_adabins(root.models_path)
depth_model.load_midas(root.models_path)

def cache_aesthetics_models(root):
    model_name = {
        "ViT-B/32": "sac_public_2022_06_29_vit_b_32_linear.pth",
        "ViT-B/16": "sac_public_2022_06_29_vit_b_16_linear.pth",
        "ViT-L/14": "sac_public_2022_06_29_vit_l_14_linear.pth",
    }
    
    for clip_name, file_name in model_name.items():
        if not os.path.exists(os.path.join(root.models_path, file_name)):
            print("Downloading aesthetics model...")
            wget.download(
                f"https://github.com/crowsonkb/simulacra-aesthetic-models/raw/master/models/{file_name}", 
                out=os.path.join(root.models_path, file_name)
            )

cache_aesthetics_models(root)

def cache_timm_models():
    model_url = "https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-weights/tf_efficientnet_b5_ap-9e82fae8.pth"
    model_path = "/root/.cache/torch/hub/checkpoints/"
    
    # Create the path if it doesn't exist
    os.makedirs(model_path, exist_ok=True)
    
    # Download the model file
    if not os.path.exists(os.path.join(model_path, "tf_efficientnet_b5_ap-9e82fae8.pth")):
        print("Downloading tf_efficientnet_b5_ap-9e82fae8.pth model...")
        wget.download(model_url, out=model_path)

def cache_gen_efficientnet():
    repo_url = "https://github.com/rwightman/gen-efficientnet-pytorch/zipball/master"
    repo_path = "/root/.cache/torch/hub/"
    zip_path = os.path.join(repo_path, "rwightman_gen-efficientnet-pytorch_master.zip")
    extract_path = os.path.join(repo_path, "rwightman_gen-efficientnet-pytorch_master")
    
    # Create the path if it doesn't exist
    os.makedirs(extract_path, exist_ok=True)

    # Download the repo zip file
    if not os.path.exists(zip_path):
        print("Downloading gen-efficientnet-pytorch source code...")
        wget.download(repo_url, out=zip_path)

    # Extract the zip file
    if not os.path.exists(os.path.join(extract_path, "setup.py")):  # assuming setup.py as an indicator of the source code
        print("Extracting gen-efficientnet-pytorch source code...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

cache_timm_models()
cache_gen_efficientnet()
