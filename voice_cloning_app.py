import tkinter as tk

# Define a class for the voice cloning application
class VoiceCloningApp:  
    def __init__(self, root_window):
        self.root_window = root_window
        root_window.title("Voice Cloning Application")
         
        # Label and entry field to enter audio file URL
        self.label = tk.label(root_window, text="Enter audio file path ")
        self.label.pack()
        
        self.entry = tk.Entry(root_window)  
        self.entry.pack()  # Pack the entry widget into the root window

        # Button to load audio file
        self.load_button = tk.Button(root_window, text="Browse", command=self.load_audio_file)  
        self.load_button.pack()  

        # Button to clone voice
        self.clone_button = tk.Button(root_window, text="Clone Voice", command=self.clone_voice)  
        self.clone_button.pack()  
        

    def load_audio_file(self):  # Method to load audio file
        # pass
        self.audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
        self.entry.insert(tk.END, self.audio_file_path)

    def clone_voice(self):  # Method to clone voice
        # pass
        synthesizer = Synthesizer()  
        vocoder = synthesizer.load_vocoder()
        
        # Load audio file and preprocess
        loader = SynthesisDataLoader(self.audio_file_path, vocoder)  # Create a SynthesisDataLoader instance
        mel_output, mel_lengths, mel_filename = loader.load_mel()  # Load mel spectrogram from audio file

        mel_output = np.expand_dims(mel_output, 0)  # Expand dimensions of mel spectrogram

        with torch.no_grad():  # Disable gradient calculation
            # Perform voice cloning
            spectrogram = synthesizer.inference(mel_output)  

        # Synthesize waveform
        waveform = vocoder.inference(spectrogram)  

        # Save the synthesized waveform
        output_path = 'synthesized_audio.wav'  # Define output file path
        sf.write(output_path, waveform.view(-1).cpu().numpy(), synthesizer.config['sampling_rate'])  

       