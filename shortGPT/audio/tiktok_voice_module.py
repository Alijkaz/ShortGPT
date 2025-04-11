from shortGPT.audio.voice_module import VoiceModule
from shortGPT.audio.tiktok_voice.src import Voice, tts
import os

class TikTokVoiceModule(VoiceModule):
    def __init__(self, voiceName):
        """
        Initialize the TikTokVoiceModule with a specified voice name.
        
        Args:
            voiceName (str): The name of the TikTok voice to use (e.g., 'en_us_001').
        """
        self.voiceName = voiceName
        # Validate voice name during initialization
        self.voice = Voice.from_string(voiceName)
        if self.voice is None:
            raise ValueError(f"Invalid TikTok voice name: {voiceName}")
        super().__init__()

    def generate_voice(self, text, outputfile):
        """
        Generate voice audio using TikTok TTS and save to outputfile.
        
        Args:
            text (str): The text to convert to speech.
            outputfile (str): The path where the output MP3 file will be saved.
        
        Returns:
            str: The path to the generated audio file.
        
        Raises:
            ValueError: If text is empty or invalid.
            Exception: If TTS generation fails.
        """
        if not text or not isinstance(text, str):
            raise ValueError("Text input must be a non-empty string")
        
        try:
            # Ensure output directory exists
            os.makedirs(os.path.dirname(outputfile), exist_ok=True)
            
            # Call TikTok TTS function (play=False to avoid playing audio)
            tts(text, self.voice, outputfile, play=False)
            
            # Verify file was created
            if not os.path.exists(outputfile):
                raise Exception("Failed to generate audio file")
            
            return outputfile
        except Exception as e:
            raise Exception(f"TikTok TTS failed: {str(e)}")