
import os
from fashn import Fashn
from dotenv import load_dotenv

load_dotenv()
 
client = Fashn(
    api_key=os.getenv("FASHN_API_KEY"),
)
 
result = client.predictions.subscribe(
    model_name="tryon-v1.6",
    inputs={
        "segmentation_free": "false",
        "mode": "quality",
        "garment_photo_type": "model",
        "garment_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/fMeHlVjqkKHa10hdt8jvgnGMk1kmwnWh/Un70_M5qhnyfpuDvi0SyfXel_QMjLt90/R27Qf964AOLoIhXCMHzs7Dnlt-gFS7_R/qFxTV2DStcA.jpeg",
        "model_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/ywCqmKO9wl5hgf3SX5C5q77wqIDTdBHR/E3fWXJIAynPaNH2M-GnrBRIXUN9GjDTa/I_UKgKr_rF_NHqtb01IFfwRc0yzaGDnu/fk1TnQz9IqQ.jpg",
        "category": 'tops'
    },
)
 
print("Generation completed!")
print("Result:", result)

#https://docs.fashn.ai/api-reference/tryon-v1-6

