import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

'''
Ali Alzurufi

This program is designed to recognize hand-written digits using machine learning algorithms with the TensorFlow library. 
It also utilizes NumPy for numerical computations and Matplotlib for data visualization. 
The goal of this program is to provide an opportunity to learn about various machine learning techniques and libraries, 
as well as to explore the possibilities of digit recognition using AI.

Date: 04/01/23
'''


# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the model architecture"
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model on the training data
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model's accuracy on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

# Make predictions on new images
images = x_test[:10]
predictions = model.predict(images)

# Loop through the images and display the predicted digit
for i in range(len(images)):
    plt.imshow(images[i], cmap='gray')
    plt.title('Predicted digit: {}'.format(np.argmax(predictions[i])))
    plt.show()
