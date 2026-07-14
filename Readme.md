# 🖼️ Image Processing with NumPy

A simple Python project that demonstrates **basic image processing operations using NumPy**, without relying on OpenCV for transformations. This project converts an image to grayscale, applies a blur filter, flips the image, and rotates it using only NumPy operations.

---

## 📌 Features

- ✅ Convert RGB image to Grayscale
- ✅ Apply 3×3 Blur Filter
- ✅ Flip Image Horizontally
- ✅ Flip Image Vertically (Function Included)
- ✅ Rotate Image by 90°
- ✅ Display processed images using Matplotlib

---

## 📂 Project Structure

```
ImageNumPy/
│── sample.jpg          # Input image
│── image_processing.py # Main Python script
│── README.md           # Project documentation
```

---

## 🛠️ Technologies Used

- Python 3.x
- NumPy
- Pillow (PIL)
- Matplotlib

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ImageNumPy.git
```

Navigate to the project folder:

```bash
cd ImageNumPy
```

Install the required libraries:

```bash
pip install numpy pillow matplotlib
```

---

## ▶️ Run the Project

```bash
python image_processing.py
```

---

## 🧠 How It Works

### 1️⃣ Load Image

The input image is loaded using Pillow and converted into a NumPy array.

```python
img = Image.open("sample.jpg")
img_array = np.array(img)
```

---

### 2️⃣ Convert to Grayscale

Uses the standard luminosity formula:

```
Gray = 0.299 × R + 0.587 × G + 0.114 × B
```

---

### 3️⃣ Blur Filter

A custom **3×3 averaging kernel** is applied manually using NumPy.

Kernel:

```
1/9 1/9 1/9
1/9 1/9 1/9
1/9 1/9 1/9
```

---

### 4️⃣ Horizontal Flip

Uses NumPy's built-in function:

```python
np.fliplr(image)
```

---

### 5️⃣ Vertical Flip

Uses:

```python
np.flipud(image)
```

---

### 6️⃣ Rotate Image

Rotates the image by **90° counterclockwise**.

```python
np.rot90(image)
```

---

## 📸 Output

The program displays four processed images:

- 🩶 Grayscale Image
- 🌫️ Blurred Image
- ↔️ Horizontally Flipped Image
- 🔄 Rotated Image

---

## 📚 Libraries

| Library | Purpose |
|----------|---------|
| NumPy | Numerical computations & image manipulation |
| Pillow | Image loading |
| Matplotlib | Display images |

---

## 🚀 Future Improvements

- Brightness Adjustment
- Contrast Enhancement
- Image Sharpening
- Edge Detection
- Gaussian Blur
- RGB Channel Separation
- Image Resizing
- Image Cropping
- Histogram Equalization
- Image Saving Feature
- Interactive Menu

---

## 🎯 Learning Outcomes

This project helps you understand:

- Image representation using NumPy arrays
- Matrix manipulation
- Convolution operations
- Kernel-based filtering
- Image transformations
- Working with grayscale images
- Basic digital image processing concepts

---

## 👨‍💻 Author

**Ashish Mewada**

AI Engineer | Python Developer | NumPy Enthusiast

GitHub: https://github.com/your-username

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀