# BGS College of Engineering and Technology - Team Phoenix  
### NITK Hackathon 2024  

## Project: Sign Language Translator for Virtual Meetings

### Team Members:
1. **Harshith Mardithaya**  
2. **Rhea Fatima Estibeiro**  
3. **Shivangi Gupta**  

---

## Problem Statement:
**Enhancing Accessibility in Virtual Banking Meetings**  
Our project addresses the need for better accessibility in virtual meetings, particularly for customers with hearing impairments. The solution we propose is a **Sign Language Translator**, which integrates real-time **Sign Language interpretation** and **Live Captions** into virtual banking environments.

---

## FlowChart:
![NITK-Hackton](https://github.com/nitkhackathon2024/BGSCET-Team-Phoneix/blob/main/artifacts/flowchart.jpeg)

---

## Solution Overview:
We leverage the **Whisper open-source model** to capture live audio during virtual meetings, transcribe it into text, and translate the text into sign language. The sign language is then displayed in real-time through video, providing hearing-impaired users with seamless engagement in virtual meetings.

**Key Features:**
- **Real-time Audio Transcription**: Transcribes live audio using Whisper.
- **Text-to-Sign Language Conversion**: Converts the transcribed text into sign language gestures.
- **Live Captions**: Displays captions along with sign language for a more comprehensive communication experience.

This inclusive platform ensures that banking customers with hearing impairments can communicate effectively in virtual meetings, enhancing customer satisfaction and accessibility.

---

## Project Structure:

```plaintext
        webapp/
        │── finalsign/
        │   └── <files>
        │── nitk.html
        │── nitk.js
        │── nitk.css
        audiotranscription.py
```

## Web UI:

To run the website, either use the **Live Server** extension or manually open `nitk.html` in your browser.

- If **Live Server** is installed, right-click on `nitk.html` and select _Open with Live Server_.
- Without Live Server, navigate to the project directory and double-click `nitk.html` to open it in your browser.

---

## Audio Transcription:

For audio transcription, ensure that **Code Runner** is installed in your VSCode setup.
open the **audiotranscription.py** file and Click the run icon to execute the code. A **GPU** is required to run the Whisper model locally, as it is computationally intensive. Wait till the model is download and you get a messaged in your terminal saying **model loaded** After that whatever you speak into your mic in 10secs to 1min depending on your GPU the trasncriptions will start being printed on your terminal

---

## Text to Sign Language:

1. In your terminal, navigate to the `finalsign` folder:

    ```bash
    cd /webapp/finalsign
    ```

2. Run the server:

    ```bash
    python server.py run server
    ```

3. Open your web browser and go to:

    ```plaintext
    localhost:8000
    ```

   Here, you can input text or sentences, and it will be translated into a coherent sign language video.**
   This feature ensures that users with hearing impairments can follow along seamlessly in virtual meetings. By providing an intuitive interface, the platform bridges the communication gap, making conversations more inclusive.
   The system processes text in real time and converts it into sign language gestures.

---

## How to Run the Project:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/nitkhackathon2024/BGSCET---Team-Phoenix.git
    ```

2. **Install Dependencies**:

    Ensure Python is installed, then install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## References:

- [Whisper Model by OpenAI](https://github.com/openai/whisper)
- [Live Server Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [Code Runner Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
- [Sign language repository](https://bslsignbank.ucl.ac.uk/)
