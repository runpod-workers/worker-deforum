INPUT_SCHEMA = {
    "model_checkpoint": {
        "type": str,
        "required": False,
        "default": "Protogen_V2.2.ckpt",
    },
    "max_frames": {
        "type": int,
        "required": False,
        "default": 200,
    },
    "animation_prompts": {
        "type": str,
        "required": False,
        "default": "0: a beautiful apple, trending on Artstation | 50: a beautiful banana, trending on Artstation | 100: a beautiful coconut, trending on Artstation | 150: a beautiful durian, trending on Artstation",
    },
    "negative_prompts": {
        "type": str,
        "required": False,
        "default": "0: mountain"
    },
    "width": {
        "type": int,
        "required": False,
        "default": 512,
    },
    "height": {
        "type": int,
        "required": False,
        "default": 512,
    },
    "num_inference_steps": {
        "type": int,
        "required": False,
        "default": 50,
        "constraints": lambda x: 1 <= x <= 500,
    },
    "guidance_scale": {
        "type": float,
        "required": False,
        "default": 7,
        "constraints": lambda x: 1 <= x <= 20,
    },
    "sampler": {
        "type": str,
        "required": False,
        "default": "euler_ancestral",
    },
    "seed": {
        "type": int,
        "required": False,
        "default": None,
    },
    "fps": {
        "type": int,
        "required": False,
        "default": 15,
        "constraints": lambda x: 10 <= x <= 60,
    },
    "clip_name": {
        "type": str,
        "required": False,
        "default": "ViT-L/14",
    },
    "use_init": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "init_image": {
        "type": str,
        "required": False,
        "default": None,
    },
    "strength": {
        "type": float,
        "required": False,
        "default": 0.5,
    },
    "use_mask": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "mask_file": {
        "type": str,
        "required": False,
        "default": None,
    },
    "invert_mask": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "animation_mode": {
        "type": str,
        "required": False,
        "default": "2D",
    },
    "border": {
        "type": str,
        "required": False,
        "default": "replicate",
    },
    "angle": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "zoom": {
        "type": str,
        "required": False,
        "default": "0:(1.04)",
    },
    "translation_x": {
        "type": str,
        "required": False,
        "default": "0:(10*sin(2*3.14*t/10))",
    },
    "translation_y": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "translation_z": {
        "type": str,
        "required": False,
        "default": "0:(10)",
    },
    "rotation_3d_x": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "rotation_3d_y": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "rotation_3d_z": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "flip_2d_perspective": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "perspective_flip_theta": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "perspective_flip_phi": {
        "type": str,
        "required": False,
        "default": "0:(t%15)",
    },
    "perspective_flip_gamma": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "perspective_flip_fv": {
        "type": str,
        "required": False,
        "default": "0:(53)",
    },
    "noise_schedule": {
        "type": str,
        "required": False,
        "default": "0: (0.02)",
    },
    "strength_schedule": {
        "type": str,
        "required": False,
        "default": "0: (0.65)",
    },
    "contrast_schedule": {
        "type": str,
        "required": False,
        "default": "0: (1.0)",
    },
    "hybrid_video_comp_alpha_schedule": {
        "type": str,
        "required": False,
        "default": "0:(1)",
    },
    "hybrid_video_comp_mask_blend_alpha_schedule": {
        "type": str,
        "required": False,
        "default": "0:(0.5)",
    },
    "hybrid_video_comp_mask_contrast_schedule": {
        "type": str,
        "required": False,
        "default": "0:(1)",
    },
    "hybrid_video_comp_mask_auto_contrast_cutoff_high_schedule": {
        "type": str,
        "required": False,
        "default": "0:(100)",
    },
    "hybrid_video_comp_mask_auto_contrast_cutoff_low_schedule": {
        "type": str,
        "required": False,
        "default": "0:(0)",
    },
    "enable_schedule_samplers": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "sampler_schedule": {
        "type": str,
        "required": False,
        "default": "0:('euler'),10:('dpm2'),20:('dpm2_ancestral'),30:('heun'),40:('euler'),50:('euler_ancestral'),60:('dpm_fast'),70:('dpm_adaptive'),80:('dpmpp_2s_a'),90:('dpmpp_2m')"
    },
    "kernel_schedule": {
        "type": str,
        "required": False,
        "default": "0: (5)",
    },
    "sigma_schedule": {
        "type": str,
        "required": False,
        "default": "0: (1.0)",
    },
    "amount_schedule": {
        "type": str,
        "required": False,
        "default": "0: (0.2)",
    },
    "threshold_schedule": {
        "type": str,
        "required": False,
        "default": "0: (0.0)",
    },
    "color_coherence": {
        "type": str,
        "required": False,
        "default": "Match Frame 0 LAB",
    },
    "color_coherence_video_every_N_frames": {
        "type": int,
        "required": False,
        "default": 1,
    },
    "diffusion_cadence": {
        "type": str,
        "required": False,
        "default": "1",
    },
    "use_depth_warping": {
        "type": bool,
        "required": False,
        "default": True,
    },
    "midas_weight": {
        "type": float,
        "required": False,
        "default": 0.3,
    },
    "near_plane": {
        "type": int,
        "required": False,
        "default": 200,
    },
    "far_plane": {
        "type": int,
        "required": False,
        "default": 10000,
    },
    "fov": {
        "type": int,
        "required": False,
        "default": 40,
    },
    "padding_mode": {
        "type": str,
        "required": False,
        "default": "border",
        "choices": ["border", "reflection", "zeros"],
    },
    "sampling_mode": {
        "type": str,
        "required": False,
        "default": "bicubic",
        "choices": ["bicubic", "bilinear", "nearest"],
    },
    "video_init_path": {
        "type": str,
        "required": False,
        "default": None,
    },
    "extract_nth_frame": {
        "type": int,
        "required": False,
        "default": 1,
    },
    "overwrite_extracted_frames": {
        "type": bool,
        "required": False,
        "default": True,
    },
    "use_mask_video": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "video_mask_path": {
        "type": str,
        "required": False,
        "default": None,
    },
    "hybrid_video_generate_inputframes": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "hybrid_video_use_first_frame_as_init_image": {
        "type": bool,
        "required": False,
        "default": True,
    },
    "hybrid_video_motion": {
        "type": str,
        "required": False,
        "default": "None",
        "choices": ["None", "Optical Flow", "Perspective", "Affine"],
    },
    "hybrid_video_flow_method": {
        "type": str,
        "required": False,
        "default": "Farneback",
        "choices": ["Farneback", "DenseRLOF", "SF"],
    },
    "hybrid_video_composite": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "hybrid_video_comp_mask_type": {
        "type": str,
        "required": False,
        "default": "None",
        "choices": ["None", "Depth", "Video Depth", "Blend", "Difference"],
    },
    "hybrid_video_comp_mask_inverse": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "hybrid_video_comp_mask_equalize": {
        "type": str,
        "required": False,
        "default": "None",
        "choices": ["None", "Before", "After", "Both"],
    },
    "hybrid_video_comp_mask_auto_contrast": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "hybrid_video_comp_save_extra_frames": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "hybrid_video_use_video_as_mse_image": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "interpolate_key_frames": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "interpolate_x_frames": {
        "type": int,
        "required": False,
        "default": 4,
    },
    "resume_from_timestring": {
        "type": bool,
        "required": False,
        "default": False,
    },
    "resume_timestring": {
        "type": str,
        "required": False,
        "default": "",
    }
}
