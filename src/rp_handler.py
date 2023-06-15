import runpod
import os
from runpod.serverless.utils import upload_file_to_bucket
import uuid
from predict import Predictor

from runpod.serverless.utils.rp_validator import validate
from rp_schema import INPUT_SCHEMA

generate_video = Predictor()
generate_video.setup()


# TODO: Missing download for path inputs (video_init_path, video_mask_path)

def handler(event):

    if (_input := event.get("input")) is None:
        return {
            "error": "INPUT_NOT_PROVIDED",
        }

    if (validated_input := validate(_input, INPUT_SCHEMA)).get("errors") is not None:
        return validated_input['errors']

    if (s3_config := event.get("s3Config")) is None:
        return {
            "error": "S3_CONFIG_NOT_PROVIDED",
        }
    if (s3_access_key_id := s3_config.get("accessId")) is None:
        return {"error": "AWS_ACCESS_KEY_ID_NOT_PROVIDED"}
    if (s3_secret_access_key := s3_config.get("accessSecret")) is None:
        return {
            "error": "AWS_SECRET_ACCESS_KEY_NOT_PROVIDED",
        }
    if (s3_bucket_name := s3_config.get("bucketName")) is None:
        return {
            "error": "BUCKET_NOT_PROVIDED",
        }

    s3_endpoint_url = s3_config.get("endpointUrl")
    s3_endpoint_url = (
        s3_endpoint_url if s3_endpoint_url else "https://s3.amazonaws.com/"
    )

    generated_video_local_path = generate_video.predict(**validated_input['validated_input'])

    file_url = upload_file_to_bucket(
        file_name=f"{uuid.uuid4()}.mp4",
        file_location=generated_video_local_path,
        bucket_creds={
            "endpointUrl": s3_endpoint_url,
            "accessId": s3_access_key_id,
            "accessSecret": s3_secret_access_key,
        },
        bucket_name=s3_bucket_name,
    )

    os.remove(generated_video_local_path)

    return {
        "version": "1.06.2023-08:08",
        "file_url": file_url,
    }


runpod.serverless.start({"handler": handler})
