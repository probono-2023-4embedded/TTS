# TTS
TTS part of MovingRobot Project, powered by Google Cloud Text-to-Speech API.

#### 별도 제공된 GCP Application Default Credentials(ADC) 파일("GCP-key.json")을 같은 경로에 놓고 실행해주세요.

Tested on Python 3.10(AMD64, Windows)

## Usage Guide
Below sample code is included in test.py

```python
from tts import VoiceType, TtsClient

# TTS 클라이언트 객체 생성
ttsClient = TtsClient()

# 음성 변경(Optional)
ttsClient.change_voice(VoiceType.Female_Standard_B)

# tts 실행
ttsClient.text_to_speech("안녕하세요!")
```

### VoiceType
```python
# TTS 목소리 선택지
class VoiceType(Enum):
    Female_Neural2_A = "ko-KR-Neural2-A"
    Female_Neural2_B = "ko-KR-Neural2-B"
    Male_Neural2_C = "ko-KR-Neural2-C"
    Female_Standard_A = "ko-KR-Standard-A"
    Female_Standard_B = "ko-KR-Standard-B"
    Male_Standard_C = "ko-KR-Standard-C"
    Male_Standard_D = "ko-KR-Standard-D"
    Female_Wavenet_A = "ko-KR-Wavenet-A"
    Female_Wavenet_B = "ko-KR-Wavenet-B"
    Male_Wavenet_C = "ko-KR-Wavenet-C"
    Male_Wavenet_D = "ko-KR-Wavenet-D"
```
