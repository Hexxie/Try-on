import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FASHN_API_KEY")

# ---------------------------
# 1. Submit try-on request
# ---------------------------

response = requests.post(
    "https://api.fashn.ai/v1/run",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    },
    json={
        "model_name": "tryon-max",
        "inputs": {
            "output_format": "jpeg",
            "product_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/dP01UUGVgf-fgyPoMQWSZ4WSj-w98dcK/Yan_NthmIn2e-46cooadKJdepOqsK9wl/2sBL_s5UW2nM0YrAnsp9sjQszFbdcEKr/g_vZ7rkjKF0.jpeg",
            "model_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/JLq66hDylpN8g4pIYTyf9KFfdDhzWFiA/EIz6AF6-G50iW3XKqC-8jqc9PGXdYxSD/iaAUF6SRKixokzDt-Jlp-5pbE5rS8tzJ/RByE3t3WNtc.jpeg",
            "prompt": "preserve model, model's face as is and location. Wear only bottom",
        },
    },
)

result = response.json()
prediction_id = result["id"]

print("Prediction ID:", prediction_id)

# ---------------------------
# 2. Poll result until done
# ---------------------------

while True:
    poll_response = requests.get(
        f"https://api.fashn.ai/v1/status/{prediction_id}",
        headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    },
    )

    poll_data = poll_response.json()
    print(poll_data)
    status = poll_data["status"]

    print("⏳ Status:", status)

    if status == "completed":
        print("\n✅ Try-on completed!")

        # Output is usually here:
        print("Result:", poll_data["output"])

        break

    elif status == "failed":
        print("\n❌ Try-on failed!")
        print(poll_data)
        break

    time.sleep(2)  # wait before next poll