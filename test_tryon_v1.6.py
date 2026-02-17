
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
        "mode": "quality",
        "garment_photo_type": "model",
        "garment_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/dP01UUGVgf-fgyPoMQWSZ4WSj-w98dcK/Yan_NthmIn2e-46cooadKJdepOqsK9wl/2sBL_s5UW2nM0YrAnsp9sjQszFbdcEKr/g_vZ7rkjKF0.jpeg",
        "model_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/k7zJHkA3dTe8xyBXY2GeblnfF5ot8Xt1/7F403DIlaygCwvDaFD7-OOcGzcJ4jqrh/cYZ4xX89Q6pG3mcdNGJCIv9fzVVn4SB2/1569W2e_IS0.png",
        "category": 'tops'
    },
)
 
print("Generation completed!")
print("Result:", result)

#https://docs.fashn.ai/api-reference/tryon-v1-6

