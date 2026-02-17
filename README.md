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
It's better fit if the cloth already on model, even if the model would be the other person.

<table>
<tr>
<th>Model</th><th>Cloth (PNG)</th><th>Result</th>
</tr>
<tr>
<td><img src="https://i.wfolio.com/x/KfN2JhbB89-m6UeUSQ-43b-4LTDPyZVn/q6sVLUvjujnOk6mXbO2srbIKpPlcOqy0/t7rVx8PT5NFW95R5iPfYgBdCvXqdZSYC/zyAGIGx14QnH8prwkbZ-T_VQC0dpw9Hp/imD7pN62XUepN3NSIwunZivpTEHlizDC/pQpcrjYZqQJvUtUt4HACGJ6AV5G3Chd9/FZ5BNwt4ycGq0LeStRaS21f0TnE0RrFR/Z5Iamix_ElOu5TXOmrIYv7rF3knZQ4QC/3X2PLPlQbFc-G1C1Az5GJYdKthKCZqJI/2pQQPSm_Lq8YlC1ilUNymXpnL6yDv43E/-V_YazcHwnhHLV53lFNdq-kSlEkslCvM/BWDJInvJ2CtJlIIkWr-dI5HIRmLTMS7d/UtuAbP6fItfLEhzRq9mrytJ_d14Hmh3p/QqM-_CWqfInq0K5KdIaeHFW8sYzL3FDu/XGUm9DXvT669P6zalkoKJv4zlwUUfAV0/mMUgBznREfyejKCDHVv7DVwu609iakpu/zGcqHSUrJs8rqTEQml4w7y7crt-u34Vx/-A1HszjUTuj3tZHsFTFh5kgEuODv9S-2/nhdwQ6KkxmJ55jDC5ZoAIA.jpg" width="240" height="360" alt="model"></td>
<td><img src="https://i.wfolio.com/x/KfN2JhbB89-m6UeUSQ-43b-4LTDPyZVn/q6sVLUvjujnOk6mXbO2srbIKpPlcOqy0/t7rVx8PT5NFW95R5iPfYgBdCvXqdZSYC/zyAGIGx14QnH8prwkbZ-T_VQC0dpw9Hp/imD7pN62XUepN3NSIwunZivpTEHlizDC/pQpcrjYZqQJvUtUt4HACGJ6AV5G3Chd9/FZ5BNwt4ycGq0LeStRaS21f0TnE0RrFR/Z5Iamix_ElOu5TXOmrIYv7rF3knZQ4QC/3X2PLPlQbFc-G1C1Az5GJf2eq-ASD7DK/rJroK6K9VCy6qg4c8Xv043FBQcslyO6b/EYNAOfLW4DU_DkbTy9iqB4Dzp16gz74S/K3rK_UIEfLv4498XS9-qTwn1JuAowYzF/YZDFhY6dopxnBb8_MxH7-B0aUaMF-bZn/zcV5GC4uE9B0umE9T506B8x5IPWW5BEm/XQ0KLvp01zxASvgd5Qx09U3GfuT9cqnW/yLQv31S3THoZfIYStVtnVwkIN3ND3rPc/_gPU8nN86-LLYVHMnsKk9qkhcCaeVInx/sAp2UAqkEb2IU_aFiqgY1QwB_LGp6AHA/jfkEKiVfFPIwUhvNwE5EtQ.png" width="240" height="360" alt="cloth"></td>
<td><img src="https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/fMeHlVjqkKHa10hdt8jvgg3NlA505Tdi/h_1qcQusyDg6hcdSnum6zcFLhGji-8q2/FHeGyOiDy9y5-Ss1JHbqflqvsaA0Ji40/XDfJansX800.png" width="240" height="360" alt="result"></td>
</tr>
<tr>
<td><img src="https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/ywCqmKO9wl5hgf3SX5C5q77wqIDTdBHR/E3fWXJIAynPaNH2M-GnrBRIXUN9GjDTa/I_UKgKr_rF_NHqtb01IFfwRc0yzaGDnu/fk1TnQz9IqQ.jpg" width="240" height="360" alt="model"></td>
<td><img src="https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/kKhJ_4CoZvHD0MsOGJG_KUD0BqHVRiOm/S1JfQ3v7RT_5y12Ynkmrkwm3ejnF3Yj4/yzUcDZO-DVlOJ-1vgP3tbHvs-5Fv30JW/XXPA-4ZQXLw1KUgqNjoehA9E8nbZL3CX.jpeg" width="240" height="360" alt="cloth"></td>
<td><img src="https://static.wfolio.com/file/AqiFFw_TXMM4LDwoI2TPSVbk9gd-1s7x/yoh_TtDt5eGETeyieELbAqr824BKVSQo/5S-Rckk8dxcxKUoYkCCq5erD-kbPcfWr/CEt0V_KdYpfHp4pXxL5bo58jsTzKt3CA/puo4ovoo4J_0u3Cy5dOfvnkdYqHE84gG/jdjbCF9Sfww.png" width="240" height="360" alt="result"></td>
</tr>
</table>

# Model
Ig: @kettril


