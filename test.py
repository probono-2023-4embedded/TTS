from tts import VoiceType, TtsClient

# TTS 클라이언트 객체 생성
ttsClient = TtsClient()

# 음성 변경(Optional)
ttsClient.change_voice(VoiceType.Female_Standard_B)

# tts 실행
ttsClient.text_to_speech("안녕하세요!")