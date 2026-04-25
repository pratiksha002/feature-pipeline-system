from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def get_preprocessing_components():
    #numerical pipeline

    num_imputer = SimpleImputer(strategy="mean")
    scaler = StandardScaler()

    #categorical pipeline
    cat_imputer = SimpleImputer(strategy="most_frequent")
    encoder = OneHotEncoder(handle_unknown="ignore")

    return num_imputer, scaler, cat_imputer, encoder
