import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe hands model.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Start capturing video from the front camera.
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def hand_is_fist(hand_landmarks):
    # Implement your logic to determine if the hand is a fist
    # This will require checking the relative positions of landmarks
    return False

def hand_is_open(hand_landmarks):
    # Implement your logic to determine if the hand is open
    # This will require checking the relative positions of landmarks
    return True


def map_screen_coordinates(landmark_x, landmark_y, video_width, video_height):
    # Map the coordinates to the screen size
    return int(landmark_x * screen_width), int(landmark_y * screen_height)

dragging = False

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks.
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger landmark position.
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            cursor_x, cursor_y = map_screen_coordinates(index_tip.x, index_tip.y, video_width, video_height)

            # Check if the hand is making a fist (for press) or open (for drag).
            if hand_is_fist(hand_landmarks):  # You need to implement hand_is_fist()
                pyautogui.click()
                dragging = False
            elif hand_is_open(hand_landmarks):  # You need to implement hand_is_open()
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
                pyautogui.moveTo(cursor_x, cursor_y)
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

    # Display the resulting image
    cv2.imshow('Gesture Mouse', image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

