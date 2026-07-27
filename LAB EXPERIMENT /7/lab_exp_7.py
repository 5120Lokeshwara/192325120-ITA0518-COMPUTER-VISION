import cv2

cap = cv2.VideoCapture("Sample.mp4")

# Get original video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.5)

# Create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Skip one frame to make it faster
    cap.read()

    # Resize
    frame = cv2.resize(frame, (width, height))

    # Save frame
    out.write(frame)

    # Display
    cv2.imshow("Fast Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()