import argparse
import os
import numpy as np
import speech_recognition as sr
import whisper
import torch

from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform


def audiototext():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="medium", help="Model to use",
                        choices=["tiny", "base", "small", "medium", "large"])
   
    parser.add_argument("--energy_threshold", default=500,
                        help="Energy level for mic to detect.", type=int)
    parser.add_argument("--record_timeout", default=2,
                        help="How real time the recording is in seconds.", type=float)
    parser.add_argument("--phrase_timeout", default=3,
                        help="How much empty space between recordings before we "
                             "consider it a new line in the transcription.", type=float)

    args = parser.parse_args()

    phrase_time = None
 
    data_queue = Queue()

    recorder = sr.Recognizer()
    
    recorder.dynamic_energy_threshold = False

    source = sr.Microphone(sample_rate=16000)

    model = args.model
    if args.model != "large":
        model = model + ".en"
    audio_model = whisper.load_model(model)

    record_timeout = args.record_timeout
    phrase_timeout = args.phrase_timeout

    transcription = ['']

    with source:
        recorder.adjust_for_ambient_noise(source)

    def record_callback(_, audio:sr.AudioData) -> None:
        """
        Threaded callback function to receive audio data when recordings finish.
        audio: An AudioData containing the recorded bytes.
        """
        data = audio.get_raw_data()
        data_queue.put(data)

    recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)

   
    print("Model loaded.\n")

    while True:
        try:
            now = datetime.now()
           
            if not data_queue.empty():
                phrase_complete = False
               
                if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                    phrase_complete = True
                
                phrase_time = now
                audio_data = b''.join(data_queue.queue)
                data_queue.queue.clear()
                
              
                audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

               
                result = audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
                text = result['text'].strip()

               
                if phrase_complete:
                    transcription.append(text)
                else:
                    transcription[-1] = text

            
                os.system('cls' if os.name=='nt' else 'clear')
                for line in transcription:
                    print(line)
              
                print('', end='', flush=True)
        
        except KeyboardInterrupt:
            break

    print("\n\nTranscription:")
    for line in transcription:
        print(line)



def audiototext2(audiofile):
    whisper.load_model("turbo")
    result = whisper.transcribe(audiofile)
    print(result)
    return result


audiototext()