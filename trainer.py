def load_train_data(path: str):
    base_path="/DeepFake_Research/data/FaceForensic/train"
    x_train=[]
    y_train=[]
    for file in os.listdir(base_path):
        if "real" in file:
            y_train.append(1)
        else:
            y_train.append(0)
    image = keras.utils.load_img(base_path+file)
    image = np.array(image)
    x_train.append(image) 
    x_train=np.array(x_train)
    y_train=np.array(y_train)
    print(y_train.shape,"||",x_train.shape)
    
def load_test_data():
    base_path="/DeepFake_Research/data/FaceForensic/test/"
    x_test=[]
    y_test=[]
    for file in os.listdir(base_path):
        if "real" in file:
            y_test.append(1)
        else:
            y_test.append(0)
    image = keras.utils.load_img(base_path+file)
    image = np.array(image)
    x_test.append(image)
    x_test=np.array(x_test)
    y_test=np.array(y_test)
    print(y_test.shape,"||",x_test.shape)

def load_validation_data():
    base_path="/DeepFake_Research/data/FaceForensic/validation"
    x_val=[]
    y_val=[]
    for file in os.listdir(base_path):
        if "real" in file:
            y_val.append(1)
        else:
            y_val.append(0)
    image = keras.utils.load_img(base_path+file)
    image = np.array(image)
    x_val.append(image)
    x_val=np.array(x_val)
    y_val=np.array(y_val)
    print(y_val.shape,"||",x_val.shape)
    
        
    
    
        