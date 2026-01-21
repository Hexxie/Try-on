# Try-on

Repository to test "wearing" functionality using the Fashn API. This project runs a small test that takes a photo of a garment and applies it onto fashion model images.

## Contents
- [test.py](test.py) — example script that runs a try-on request using the `Fashn` client.
- [.env](.env) — environment file that should contain `FASHN_API_KEY`.

## Purpose
This code tests the Fashn "tryon-v1.6" model to render a photo of your clothing onto fashion model images. The script demonstrates how to create a client (see [`client`](test.py)) and how the response is stored (see [`result`](test.py)).

## Setup
1. Install dependencies:
```sh
pip install fashn python-dotenv
```

2. Add your API key to .env: 
```sh
FASHN_API_KEY="your_api_key_here"
```

3. Run
```sh
python test.py
```

## Example

Below is a quick preview showing a model image, a cloth PNG, and the composed result (model + cloth = result).

<table>
<tr>
<th>Model</th><th>Cloth (PNG)</th><th>Result</th>
</tr>
<tr>
<td><img src="https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSdxbQbO-QKTS/OPQIAHCsuC1lHhGmttk1yz3fMj_0EWJ3/AcOcixxwWIgHQcuHIH5bd7GR1_nz_ibZ/gnJEFgjY65KwODoZUC9327qDK0Ij_RZ9/5DJgdEs_K8X5Qw8AEhJ4RVl1LX5vvSd7/1K4FzuM0n4U.jpg" width="240" height="360" alt="model"></td>
<td><img src="https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSdxbQbO-QKTS/OPQIAHCsuC1lHhGmttk1yz3fMj_0EWJ3/gcpttuNoXfJ3DafUHeUXSY-J7ZOKFSI3/BNZmke_z7KcxbNtj1P8LT3ZIBxUoyNFI/U_dtLAuNrQ79PR6ePXyPShOffzRCpZp5/POD_zTll3pk.png'width="240" height="360" alt="cloth"></td>
<td><img src="https://cdn.fashn.ai/f54d0d7d-e48a-462a-b687-c0dc57736c17/output_0.png' width="240" height="360" alt="result"></td>
</tr>
</table>

# Model
Ig: @kettril
