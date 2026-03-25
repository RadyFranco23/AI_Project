import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def postprocess_custom_vision(output, labels, threshold=0.5):
    # Output viene como (H, W, C)
    # C = number of anchors * (5 + number_of_classes)
    
    H, W, C = output.shape
    num_classes = len(labels)
    num_anchors = C // (5 + num_classes)

    output = output.reshape((H, W, num_anchors, 5 + num_classes))

    detections = []

    for y in range(H):
        for x in range(W):
            for a in range(num_anchors):
                bx, by, bw, bh, conf = output[y, x, a, :5]

                conf = sigmoid(conf)

                if conf < threshold:
                    continue

                class_scores = sigmoid(output[y, x, a, 5:])
                class_id = np.argmax(class_scores)
                class_conf = class_scores[class_id] * conf

                if class_conf < threshold:
                    continue

                # Convert box from cell coords → image coords
                cx = (x + sigmoid(bx)) / W
                cy = (y + sigmoid(by)) / H
                w = np.exp(bw) / W
                h = np.exp(bh) / H

                detections.append({
                    "tagName": labels[class_id],
                    "probability": float(class_conf),
                    "boundingBox": {
                        "left": float(cx - w / 2),
                        "top": float(cy - h / 2),
                        "width": float(w),
                        "height": float(h)
                    }
                })

    return detections
