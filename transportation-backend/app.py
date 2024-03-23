from flask import Flask, request, jsonify, send_from_directory
import cv2
import os
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_DIR'] = os.path.join(os.getcwd(), 'processed_images')

@app.route("/")
def index():
    return 'Hello World!'

@app.route('/uploads', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Save the uploaded image
        filename = 'uploads/' + file.filename
        file.save(filename)

        # Process the image (Object Detection)
        processed_image = process_image(filename)

        if processed_image:
            return jsonify({'image' : processed_image})
        else:
            return jsonify({'error': 'Image processing failed'})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})

 
def process_image(filename):
    try:
        if not os.path.exists(filename):
            return None

        image = cv2.imread(filename)
        if image is None:
            return None

        xml_dir = 'classifiers/'
        xml_files = [file for file in os.listdir(xml_dir) if file.endswith('.xml')]

        for xml_file in xml_files:
            # Load the Haar cascade classifier
            car_cascade = cv2.CascadeClassifier(os.path.join(xml_dir, xml_file)) 
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Use a pre-trained Haar Cascade classifier for vehicle detection
            cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            vehicle_counts = {'car': 0, 'truck': 0, 'bus': 0}
            # Draw rectangles around detected vehicles
            for (x, y, w, h) in cars:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
                if w < 50 and h < 50:
                    vehicle_counts['car'] += 1
                    cv2.putText(image, 'Car: ' + str(vehicle_counts['car']), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                elif w < 70 and h < 70:
                    vehicle_counts['truck'] += 1
                    cv2.putText(image, 'truck: ' + str(vehicle_counts['truck']), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                else: 
                    vehicle_counts['bus'] += 1
                    cv2.putText(image, 'bus: ' + str(vehicle_counts['bus']), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        print("FILE", filename)
        processed_filename = str(time.time()) + os.path.basename(filename)
        processed_file_path = os.path.join(app.config['UPLOAD_DIR'], processed_filename)
        cv2.imwrite(processed_file_path, image)
        print("PROCESSED", processed_file_path)
        return processed_filename
    except Exception as e:
        print('Error processing image:', e)
        return None

@app.route('/processed/<file_name>', methods=['GET'])
def get_processed_image(file_name):
    return send_from_directory(app.config['UPLOAD_DIR'], file_name)
if __name__ == '__main__':
    app.run(debug=True)


