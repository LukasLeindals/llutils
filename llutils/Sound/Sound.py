class Sound:
    """
    Class to hold and use a sound object
    """

    def __init__(self, fname):
        self.fname = fname

    def play(self):
        # from playsound import playsound
        # playsound(self.fname)
        
        from pydub import AudioSegment
        from pydub.playback import play

        sound = AudioSegment.from_wav(self.fname)
        play(sound)

if __name__ == "__main__":
    sound = Sound("././test_files/Cartoon-02.wav")
    sound.play()