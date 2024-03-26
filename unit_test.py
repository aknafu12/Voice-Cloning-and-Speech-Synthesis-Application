from voice_cloning_app import VoiceCloningApp
import tkinter as tk
class TestVoiceCloningApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = VoiceCloningApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_load_audio_file(self):
        # Test loading an audio file
        audio_file_path = 'path/to/test_audio_file.wav'
        self.app.entry.insert(tk.END, audio_file_path)
        self.app.load_audio_file()
        self.assertEqual(self.app.audio_file_path, audio_file_path)

    def test_clone_voice(self):
        # Test cloning voice from an audio file
        audio_file_path = 'path/to/test_audio_file.wav'
        self.app.entry.insert(tk.END, audio_file_path)
        self.app.load_audio_file()
        self.app.clone_voice()

        # Check if synthesized audio file is created
        synthesized_audio_path = 'synthesized_audio.wav'
        self.assertTrue(sf.exists(synthesized_audio_path))

        # Clean up by deleting the synthesized audio file
        sf.delete(synthesized_audio_path)

if __name__ == '__main__':
    unittest.main()