from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

def create_overlay_button(parent, text, overlay_text):
    button = QPushButton(parent)
    button.setStyleSheet("QPushButton { background-color: red; }")
    button.setFixedSize(252, 100)  # Change the size as needed
    
    # Create a label with transparent background and center alignment
    label = QLabel(overlay_text, button)
    label.setStyleSheet("QLabel { background-color: transparent; color: white; }")
    label.setAlignment(Qt.AlignCenter)
    label.setFixedSize(button.size())
    label.move(0, 0)  # Move the label to overlay the button
    
    return button, label  # Return both the button and the label

app = QApplication([])

# Create the main widget
widget = QWidget()

# Create a QVBoxLayout
layout = QVBoxLayout(widget)

# Add buttons with overlay text
button_with_overlay1, label1 = create_overlay_button(widget, 'Button 1', '00:04:30\n50 mb.')
button_with_overlay2, label2 = create_overlay_button(widget, 'Button 2', '00:05:00\n60 mb.')
layout.addWidget(button_with_overlay1)
layout.addWidget(button_with_overlay2)

# Add a normal button without overlay text
normal_button = QPushButton('Normal Button', widget)
normal_button.setFixedSize(252, 100)  # Change the size as needed
layout.addWidget(normal_button)

# Show the main widget
widget.setLayout(layout)
widget.show()

# Start the application's event loop
app.exec_()
