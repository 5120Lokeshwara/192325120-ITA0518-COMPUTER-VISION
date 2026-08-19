import cv2
import matplotlib.pyplot as plt

# ==========================================
# THRESHOLD EFFECT IN EDGE DETECTION
# ==========================================

# Step 1: Read the input image
image = cv2.imread("1 Input.png ")

# Check if image was loaded
if image is None:
    print("Error: Could not find input.jpg")
    print("Make sure the image is in the same folder as this Python file.")
    exit()

# Step 2: Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur
# This reduces unwanted noise
blur = cv2.GaussianBlur(gray, (5, 5), 1.0)

# Step 4: Apply Canny Edge Detection
# using different threshold values

edge_30_60 = cv2.Canny(blur, 30, 60)
edge_50_100 = cv2.Canny(blur, 50, 100)
edge_100_200 = cv2.Canny(blur, 100, 200)
edge_150_300 = cv2.Canny(blur, 150, 300)

# Step 5: Display all results
plt.figure(figsize=(15, 10))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Grayscale Image
plt.subplot(2, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

# Low Threshold
plt.subplot(2, 3, 3)
plt.imshow(edge_30_60, cmap="gray")
plt.title("Threshold (30, 60) - Low")
plt.axis("off")

# Medium Threshold
plt.subplot(2, 3, 4)
plt.imshow(edge_50_100, cmap="gray")
plt.title("Threshold (50, 100) - Medium")
plt.axis("off")

# High Threshold
plt.subplot(2, 3, 5)
plt.imshow(edge_100_200, cmap="gray")
plt.title("Threshold (100, 200) - High")
plt.axis("off")

# Very High Threshold
plt.subplot(2, 3, 6)
plt.imshow(edge_150_300, cmap="gray")
plt.title("Threshold (150, 300) - Very High")
plt.axis("off")

plt.tight_layout()
plt.show()

# ==========================================
# EDGE PIXEL ANALYSIS
# ==========================================

results = {
    "(30, 60) - Low": edge_30_60,
    "(50, 100) - Medium": edge_50_100,
    "(100, 200) - High": edge_100_200,
    "(150, 300) - Very High": edge_150_300
}

print("\nTHRESHOLD EFFECT ANALYSIS")
print("=" * 50)

for name, edges in results.items():

    edge_pixels = cv2.countNonZero(edges)

    total_pixels = edges.shape[0] * edges.shape[1]

    percentage = (edge_pixels / total_pixels) * 100

    print("\nThreshold:", name)
    print("Edge Pixels:", edge_pixels)
    print("Edge Percentage:", round(percentage, 2), "%")