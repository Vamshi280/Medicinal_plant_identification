## Project Structure

The project contains the following files and directories:

1. **Folder**: Contains the code for the web interface and backend built using Django.
    - This includes all the necessary files for the server, view logic, and handling requests for plant identification.

2. **Python Notebooks**:
    - **Medicinal_plant_mahi.ipynb**: 
        - This Jupyter notebook contains the code for training the model using a Convolutional Neural Network (CNN) architecture.
        - The CNN model is specifically designed to classify medicinal plant leaves.
    - **medicin-mahi.ipynb**:
        - This notebook contains code for training the model using the MobileNet CNN architecture.
        - MobileNet is used here to achieve a more efficient and lightweight model for plant classification.
    - **identify_plant.ipynb**:
        - This notebook uses the previously trained models to identify plants from images.
        - It includes code to load the trained model and classify new plant images provided by the user.
     
  
## Project Overview

This project focuses on the identification of medicinal plants using deep learning techniques. Below are the key aspects of the project:

1. **Model Training**:
    - Initially, we trained a model using a **Convolutional Neural Network (CNN)** architecture to classify medicinal plant leaves.
    - Afterward, we experimented with a more optimized model using the **MobileNet** architecture to improve performance and reduce model size.
    - All training was done in **Jupyter Notebooks** for ease of experimentation and visualization.

2. **Web Interface**:
    - We developed a user-friendly interface for users to upload images of plants for identification.
    - The front end was created using **HTML**, **CSS**, **JavaScript**, and **Bootstrap** for responsiveness and design.

3. **Backend Development**:
    - The backend of the application is powered by **Django**, a high-level Python web framework.
    - The trained models are deployed in the backend so that when a user uploads a plant image, the backend processes the image and uses the trained model to identify the plant species.

4. **Deployment**:
    - The user interface and backend are integrated, allowing users to interact with the model in real time.
    - When an image is uploaded, the backend identifies the plant and returns the result to the user.

### Summary:
- **First Model**: CNN architecture trained for plant classification.
- **Second Model**: MobileNet-based CNN for better performance.
- **Frontend**: Built using HTML, CSS, JavaScript, and Bootstrap.
- **Backend**: Powered by Django, with models deployed to process plant identification.


![p_home](https://github.com/user-attachments/assets/546f0140-8675-4453-8fd5-f3ca5388d365)
___________________________________Home_page______________________________________________
![p_model](https://github.com/user-attachments/assets/2d165e2e-abbf-44cd-819a-386687425dcc)
___________________________________Model_page______________________________________________
![p_blog](https://github.com/user-attachments/assets/dbbf0f4e-407e-49e5-8644-1145e43ff748)
___________________________________Blog_page______________________________________________




