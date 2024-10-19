function convertText() {
    const inputText = document.getElementById("textInput").value.trim().toLowerCase();
    
    // Clear the previous video results
    const videoContainer = document.getElementById("videoContainer");
    videoContainer.innerHTML = '';

    if (!inputText) {
        alert("Please enter text.");
        return;
    }

    // Define specific phrases (like "thankyou") that should be handled as a single video
    const phraseDictionary = {
        "thankyou": "videos/thank.mp4",
        "drop off":"videos/abandon.mp4",
        "go over":"videos/above.mp4",
        "at last":"videos/finally.mp4",
        "got it":"videos/finally.mp4",
        "about time":"videos/finally.mp4",
        "sort out":"videos/manage.mp4",
        // Add more phrases here
    };

    // Check if the input text matches any specific phrases (like "thankyou")
    if (phraseDictionary.hasOwnProperty(inputText)) {
        const videoPath = phraseDictionary[inputText];
        playSeamlessVideos([videoPath], videoContainer);
    } else {
        // If no matching phrase is found, split the input into words
        const words = inputText.split(" ");
        const videoPaths = [];

        // Fetch video paths for each word
        const promises = words.map(word => 
            fetch(`/get_video/${word}`)
            .then(response => {
                if (response.ok) {
                    return response.text();
                } else {
                    throw new Error('Sign language video not found for: ' + word);
                }
            })
            .then(videoPath => {
                videoPaths.push(videoPath);
            })
            .catch(error => {
                console.error(error);
            })
        );

        // Once all videos are fetched, play them seamlessly
        Promise.all(promises).then(() => {
            if (videoPaths.length > 0) { // Check if there are valid paths
                playSeamlessVideos(videoPaths, videoContainer);
            } else {
                alert("No videos available for the entered words.");
            }
        });
    }
}

// Helper function to play videos seamlessly
function playSeamlessVideos(videoPaths, videoContainer) {
    let currentIndex = 0;

    function playNextVideo() {
        if (currentIndex < videoPaths.length) {
            const videoElement = document.createElement("video");
            videoElement.src = videoPaths[currentIndex];
            videoElement.autoplay = true;
            videoElement.controls = false; // Can set to true if you want user controls
            videoElement.width = 320;
            videoElement.muted = true; // Mute to avoid glitches in sound if any
            videoElement.style.display = "none"; // Preload the video in the background

            videoContainer.innerHTML = '';
            videoContainer.appendChild(videoElement);

            // Increase playback speed to 2x
            videoElement.playbackRate = 2;

            // Start playing the video once it's ready to avoid gaps
            videoElement.addEventListener('canplay', () => {
                videoElement.style.display = "block";
                videoElement.play();  // Play the video once ready
            });

            // When the current video ends, preload the next video and play it
            videoElement.addEventListener('ended', () => {
                currentIndex++;
                playNextVideo(); // Start the next video immediately after the current one ends
            });
        }
    }

    // Start the sequence
    playNextVideo();
}
