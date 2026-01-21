
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
        "garment_image": "https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSdxbQbO-QKTS/OPQIAHCsuC1lHhGmttk1yz3fMj_0EWJ3/gcpttuNoXfJ3DafUHeUXSY-J7ZOKFSI3/BNZmke_z7KcxbNtj1P8LT3ZIBxUoyNFI/U_dtLAuNrQ79PR6ePXyPShOffzRCpZp5/POD_zTll3pk.png",
        "model_image": "https://cdn.fashn.ai/0c4576de-99fd-4544-8e42-d63ab405ecf7/output_0.png",
    },
)
 
print("Generation completed!")
print("Result:", result)

