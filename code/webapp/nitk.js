const localVideo = document.getElementById('localVideo');
const muteBtn = document.getElementById('muteBtn');
const videoBtn = document.getElementById('videoBtn');
const leaveBtn = document.getElementById('leaveBtn');
const invertBtn = document.getElementById('invertBtn');
const captionsDiv = document.getElementById('captions');
const signLanguageContainer = document.getElementById('signLanguageContainer');
const toggleSignLangCaptions = document.getElementById('toggleSignLangCaptions');
const toggleText = document.getElementById('toggleText');

let isMirrored = false;
let localStream;

// Get the user's media (video & audio)
navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
        localVideo.srcObject = stream;
        localStream = stream;
    })
    .catch(error => {
        console.error('Error accessing media devices.', error);
    });

// Toggle video mirroring on button click
invertBtn.addEventListener('click', () => {
    isMirrored = !isMirrored;

    if (isMirrored) {
        localVideo.style.transform = 'scaleX(-1)';
    } else {
        localVideo.style.transform = 'scaleX(1)';
    }
});

// Mute/Unmute button
muteBtn.addEventListener('click', () => {
    const audioTrack = localStream.getAudioTracks()[0];
    audioTrack.enabled = !audioTrack.enabled;
    muteBtn.textContent = audioTrack.enabled ? 'Mute' : 'Unmute';
});

// Stop/Start video button
videoBtn.addEventListener('click', () => {
    const videoTrack = localStream.getVideoTracks()[0];
    videoTrack.enabled = !videoTrack.enabled;
    videoBtn.textContent = videoTrack.enabled ? 'Stop Video' : 'Start Video';
});

// Leave the call
leaveBtn.addEventListener('click', () => {
    localStream.getTracks().forEach(track => track.stop());
    localVideo.srcObject = null;
});

toggleSignLangCaptions.addEventListener('change', () => {
    if (toggleSignLangCaptions.checked) {
        captionsDiv.style.display = 'block';  // Show captions
        signLanguageContainer.style.display = 'flex';  // Show sign language container
        toggleText.textContent = 'On';
    } else {
        captionsDiv.style.display = 'none';  // Hide captions
        signLanguageContainer.style.display = 'none';  // Hide sign language container
        toggleText.textContent = 'Off';
    }
});

const signLanguageVideoUrl = "https://bslsignbank.ucl.ac.uk/media/bsl-video/DR/DROP.mp4";
const signLanguageVideo = document.getElementById('signLanguageVideo');
signLanguageVideo.src = signLanguageVideoUrl;
