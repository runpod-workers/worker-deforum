<div align="center">

<h1>Deforum | RunPod Worker</h1>

</div>

## Usage

Example:

```JSON
{
    "s3Config": {
        "accessId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "accessSecret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "bucketName": "your-bucket-name",
        "endpointUrl": "https://example.com"
    },
    "input": {
        "animation_prompts": "0: a beautiful ball, trending on Artstation | 5: a beautiful monkey, trending on Artstation",
        "max_frames": 10
    }
}
```

## Custom Model

Models are grabbed during Docker build by the `cache_model.py` file, this can be modified to use different models.
