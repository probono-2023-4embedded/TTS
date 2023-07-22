import os
from enum import Enum
from google.cloud import texttospeech
import playsound

# Google Cloud Platform 키 설정
cur_file_dir: str = str(os.path.dirname(os.path.abspath(__file__)))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cur_file_dir + "/GCP-key.json"

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

class TtsClient():
    def __init__(self) -> None:
        # TTS 클라이언트 초기화
        self.client = texttospeech.TextToSpeechClient()
        self.audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        self.voice_type = texttospeech.VoiceSelectionParams(language_code="ko-KR", name=VoiceType.Male_Standard_C.value)
    
    def change_voice(self, voiceType: VoiceType):
        self.voice_type = texttospeech.VoiceSelectionParams(language_code="ko-KR", name=voiceType.value)

    def text_to_speech(self, input: str):
        synthesis_input = texttospeech.SynthesisInput(text=input)
        response = self.client.synthesize_speech(input=synthesis_input, voice=self.voice_type, audio_config=self.audio_config)

        with open(cur_file_dir + "/output.mp3", "wb") as out:
            out.write(response.audio_content)
      
        playsound.playsound(cur_file_dir + "/output.mp3")

if __name__ == "__main__":
    # TTS 클라이언트 객체 생성
    ttsClient = TtsClient()
    
    # tts 실행
    ttsClient.text_to_speech("안녕하세요.")

    # 음성 변경
    ttsClient.change_voice(VoiceType.Female_Standard_A)
    ttsClient.text_to_speech("안녕하세요.")