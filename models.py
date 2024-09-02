from classification_models.keras import Classifiers
from tensorflow import keras

def get_models(model: str):
    SIZE = 299
    DIM = (SIZE, SIZE, 3)
    BATCH_SIZE = 150
    if model=="xception_GRU":
        
        n_classes = 1
        net, preprocess_input = Classifiers.get('xception')
        base_model = net(input_shape=DIM, weights='imagenet', include_top=False)
        x = keras.layers.GlobalAveragePooling2D()(base_model.output)
        x = keras.layers.Reshape((1, -1))(x)
        x = GRU(64)(x)
        output = keras.layers.Dense(n_classes, activation='sigmoid')(x)
        model = keras.models.Model(inputs=[base_model.input], outputs=[output])
    
    if model=="mobile_net" :
        
return model
        
         
    