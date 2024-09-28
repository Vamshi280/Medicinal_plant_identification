from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

#model 
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import os
from django.conf import settings

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from PIL import Image
import numpy as np
import json
from django.conf import settings

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from PIL import Image
import numpy as np
import json
from django.conf import settings

def predict(request):
    if request.method == 'POST' and request.FILES['image']:
        # Save the uploaded image
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        # Load the image for prediction
        image_path = fs.path(filename)
        img = Image.open(image_path)
        img = img.resize((224, 224))  # Resize image to match model input size
        img_array = np.array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        
        # Load your model and class names
        model_path = settings.MODELS_DIR / 'Model_Mobilenet.h5'
        class_names_path = settings.MODELS_DIR / 'class_names.json'

        model = tf.keras.models.load_model(str(model_path))

        with open(class_names_path, 'r') as f:
            class_names = json.load(f)
        
        predictions = model.predict(img_array)
        
        # Process the predictions
        predicted_class = np.argmax(predictions[0])
        prediction = class_names[predicted_class]  # Accessing with integer index
        
        # Render the template with the prediction result
        return render(request, 'home.html', {
            'prediction': prediction,
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')

