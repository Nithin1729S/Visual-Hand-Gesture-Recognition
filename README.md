# Real-Time American Sign Language Gesture Recognition

## Overview

This project aims to recognize American Sign Language (ASL) gestures in real-time using Python, OpenCV, and MediaPipe. The system employs computer vision techniques to interpret hand gestures, facilitating communication through ASL.

## Dependencies

Ensure you have the following dependencies installed before running the project:

- Python
- OpenCV
- MediaPipe

# Usage

To run the project, follow these steps:

1. Ensure you have Python installed on your system.

2. Install the required dependencies using the following command:

    ```bash
    pip install opencv-python mediapipe
    ```

3. Execute the main script by running the command:

    ```bash
    python main.py
    ```

This will launch the real-time hand gesture recognition application, allowing you to interact with the system using American Sign Language gestures.

# How It Works

The project utilizes a combination of Python, OpenCV, and MediaPipe to achieve real-time American Sign Language (ASL) gesture recognition. Here's an overview of how the system operates:

1. **Hand Landmark Detection:**
   - The MediaPipe library is employed to detect and track key hand landmarks in real-time.

2. **Gesture Recognition Model:**
   - The detected hand landmarks are fed into a custom-built gesture recognition model implemented in `function.py`.

3. **ASL Gesture Classification:**
   - The model classifies ASL gestures based on the positions of hand landmarks.

4. **Real-time Interaction:**
   - The main script, `main.py`, continuously processes video frames, allowing users to interact with the system using ASL gestures in real-time.

Feel free to explore and modify the code in `main.py` and other components to enhance or customize the gesture recognition system.
