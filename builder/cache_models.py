import sys

from types import SimpleNamespace
from helpers.model_load import load_model, get_model_output_paths

sys.path.insert(0, "src")


def PathSetup():
    models_path = "diffusion_models_cache"  # @param {type:"string"}
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
