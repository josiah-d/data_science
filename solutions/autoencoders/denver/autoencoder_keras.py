from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

class Autoencoder(object):
    
    def __init__(self, inout_dim, encoded_dim):    
        input_layer = Input(shape=(inout_dim,))
        hidden_input = Input(shape=(encoded_dim,))
        hidden_layer = Dense(encoded_dim, activation='relu')(input_layer)
        output_layer = Dense(inout_dim, activation='sigmoid')(hidden_layer)
        
        self._autoencoder_model = Model(input_layer, output_layer)
        self._encoder_model = Model(input_layer, hidden_layer)
        tmp_decoder_layer = self._autoencoder_model.layers[-1]
        self._decoder_model = Model(hidden_input, tmp_decoder_layer(hidden_input))
        # changed optimizer to adam for better performance 
        self._autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')
        
    def train(self, input_train, input_test, batch_size, epochs):    
        self._autoencoder_model.fit(input_train, 
                                    input_train,
                                    epochs = epochs,
                                    batch_size=batch_size,
                                    shuffle=True,
                                    validation_data=(
                                            input_test, 
                                            input_test))
        
    def getEncodedImage(self, image):
        encoded_image = self._encoder_model.predict(image)
        return encoded_image
    
    def getDecodedImage(self, encoded_imgs):
        decoded_image = self._decoder_model.predict(encoded_imgs)
        return decoded_image
