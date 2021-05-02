# Hack-At-Home-II

## Description

In third-world countries like India, recyclable and non-recyclable waste is usually misclassified and even a lot of people don't remember where their trash should go. Trash Misclassifications can even have a major impact on increasing greenhouse emissions, which further contribute to climate change. To solve this problem, I'm presenting a smart bin that is currently using my laptop's webcam to take an image of the material, and then it sends that image to Google Cloud. With the help of Google's CloudVision API, it identifies what is there in the image and returns it to my client. Depending upon the name of that object, my program classifies it as either trash or recyclable material and then opens up one compartment accordingly.

## Installation
Arduino IDE can be installed from <a href = "https://www.arduino.cc/en/software">this link</a>.

For installing OpenCV:
```
pip install opencv-python
```

## Tech Stack
<ul>
  <li>C++ (Arduino)</li>
  <li>Python (OpenCV, Basic)</li>
  <li>Google CloudVision</li>
  <li>Internet of Things</li>
</ul>

## Future Scope
I'll be making it a fully independent setup that will use Raspberry Pi and its camera, instead of an Arduino with my laptop's webcam.

