
import os
import cv2
from ultralytics import YOLO

def processImage():
    image_path = "./crack.jpg"
    image = cv2.imread(image_path)

    model_path = os.path.join('.', 'best.pt') # here, '.' means the root directory 
    model = YOLO(model_path)

    threshold = 0.5

    results = model(image)[0]

    print(type(results))
    text = None
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

            class_label = results.names[int(class_id)].upper()

            text = f"{class_label}: {score:.2f}"

            cv2.putText(image, text, (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return text
print(processImage())