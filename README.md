"## Parking Spot Detection 🚗🅿️

This project detects empty and occupied parking spots from a video using computer vision techniques.

## 🔍 Features
- Detects parking spaces using a binary mask and connected components.
- Determines whether each spot is occupied or free.
- Displays real-time detection using colored bounding boxes:
  - 🟥 Red for **occupied**
  - 🟩 Green for **empty**
- Shows a video feed with spot status overlayed.

## 📁 Files
- \`parking_1920_1080_loop.mp4\`: Input video of the parking lot.
- \`mask_1920_1080.png\`: Binary mask that defines the parking spots.
- \`util.py\`: Helper functions (e.g., to check spot occupancy).
- \`main.py\`: Main script that runs the detection.

## 📦 Libraries Used
- OpenCV
- NumPy
- Pandas (optional)

## ▶️ How to Run
1. Clone this repo
2. Make sure \`parking_1920_1080_loop.mp4\` and \`mask_1920_1080.png\` are in the same directory
3. Run:
   \`\`\`
   python main.py
   \`\`\`

## ✨ Output
Each parking spot is monitored live and visual feedback is given via bounding boxes.

## 📌 Note
Make sure you have OpenCV installed:
\`\`\`
pip install opencv-python
\`\`\`

" > README.md && git add README.md && git commit -m "Add README for parking spot detection project" && git push
