import cv2
import mediapipe as mp

# Initialize MediaPipe hands model.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5)

# Initialize MediaPipe drawing utils for drawing hands landmarks on the image.
mp_drawing = mp.solutions.drawing_utils

# Start capturing video from the front camera.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    # Convert the BGR image to RGB.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks.
    result = hands.process(rgb_frame)

    # Draw the hand annotations on the frame.
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame.
    cv2.imshow('Finger Gesture Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all active windows.
cap.release()
cv2.destroyAllWindows()
