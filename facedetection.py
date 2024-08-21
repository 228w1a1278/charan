import cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press '1' to capture a photo or 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('1'):
            filename = 'captured_image.jpg'
            cv2.imwrite(filename, frame)
            print(f"Photo saved as {filename}.")
        elif key == ord('q'):
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
