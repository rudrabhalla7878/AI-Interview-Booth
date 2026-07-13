import speech_recognition as sr

def get_audio_input():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("🎙️ Speak now...")

        try:
            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=20
            )

            text = recognizer.recognize_google(audio)

            return text

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""

        except sr.RequestError:
            print("Speech Recognition service unavailable.")
            return ""

        except Exception as e:
            print("Error:", e)
            return ""