from ovos_plugin_manager.templates.tts import TTS


# base plugin class
class MyTTSPlugin(TTS):
    def __init__(self, *args, **kwargs):
        # in here you should specify if your plugin return wav or mp3 files
        # you should also specify any valid ssml tags
        ssml_tags = ["speak", "s", "w", "voice", "prosody",
                     "say-as", "break", "sub", "phoneme"]
        super().__init__(*args, **kwargs, audio_ext="wav", ssml_tags=ssml_tags)
        # read config settings for your plugin if any
        self.pitch = self.config.get("pitch", 0.5)

    def get_tts(self, sentence, wav_file):
        # TODO - create TTS audio @ wav_file (path)
        return wav_file, None

    @property
    def available_languages(self):
        """Return languages supported by this TTS implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        # TODO - what langs can this TTS handle?
        return {"en-us", "es-es"}


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all other keys represent an example valid config for the plugin
MyTTSConfig = {
    lang: [{"lang": lang,
            "display_name": f"MyTTS ({lang}",
            "priority": 70,
            "offline": True}]
    for lang in ["en-us", "es-es"]
}
