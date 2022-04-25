import cv2


def overlayShadow(img, pattern, shadow_intensity=53):
    if pattern.shape[-1] == 1 or len(pattern.shape) == 2:
        pattern = cv2.cvtColor(pattern, cv2.COLOR_GRAY2BGR)

    pattern = cv2.resize(pattern, tuple(reversed(img.shape[:2])))
    pattern = cv2.bitwise_not(pattern)
    shadow  = cv2.addWeighted(pattern, 0, pattern, 1, shadow_intensity-300)

    return cv2.subtract(img, shadow)

if __name__ == "__main__":
    image  = cv2.imread("photos/paper.png")
    shadow = cv2.imread("photos/shadow3.png")

    output = overlayShadow(image, shadow)

    cv2.imshow('Overlayed Shadow', output)
    cv2.waitKey(0)