from src.train import train_model

def main():
    print("Starting feature engineering pipeline system...")

    model, pipeline = train_model()

    print("Training completed.")
    print("Model and pipeline saved")

if __name__ == "__main__":
    main()