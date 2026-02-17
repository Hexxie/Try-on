import requests
import time
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FASHN_API_KEY")

while True:
    poll_response = requests.get(
        f"https://api.fashn.ai/v1/status/271f3310-3d31-4b08-a454-eff254330617",
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