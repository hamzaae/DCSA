import joblib

def load_model(model_path):
    """Load a model from a file path."""
    return joblib.load(model_path)

def save_model(model, model_path):
    """Save a model to a file path."""
    joblib.dump(model, model_path)

def model_predict(model, X):
    """Make predictions on a set of data."""
    return model.predict(X)

def model_predict_proba(model, X):
    """Make probability predictions on a set of data."""
    return model.predict_proba(X)
