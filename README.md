# 🏨 Hotel Reservation Prediction - MLOps Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![LightGBM](https://img.shields.io/badge/LightGBM-3.0+-green.svg)](https://lightgbm.readthedocs.io/)
[![MLflow](https://img.shields.io/badge/MLflow-2.0+-red.svg)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red.svg)](https://www.jenkins.io/)

> A comprehensive MLOps solution for predicting hotel reservation outcomes using machine learning, featuring automated pipelines, web deployment, and production-ready infrastructure.

## 🚀 Overview

This project demonstrates end-to-end MLOps practices by building a predictive model for hotel reservation cancellations. The system ingests data from Google Cloud Storage, trains a LightGBM model with hyperparameter optimization, and deploys a user-friendly web application for real-time predictions.

### 🎯 Key Highlights
- **Production-Ready Architecture**: Modular design with separation of concerns
- **Automated ML Pipeline**: Data ingestion, preprocessing, training, and deployment
- **Web Interface**: Intuitive Flask application for model predictions
- **MLOps Best Practices**: Logging, error handling, configuration management
- **Cloud Integration**: GCP Storage for data management
- **CI/CD Ready**: Jenkins pipeline for automated testing and deployment
- **Containerization**: Docker support for easy deployment

## 🛠️ Tech Stack

### Core Technologies
- **Backend**: Python 3.8+, Flask
- **Machine Learning**: LightGBM, scikit-learn, imbalanced-learn
- **Data Processing**: pandas, numpy
- **Experiment Tracking**: MLflow
- **Cloud Storage**: Google Cloud Storage
- **Configuration**: PyYAML
- **Logging**: Python logging with custom handlers

### DevOps & Deployment
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Version Control**: Git
- **Package Management**: pip, setuptools

## 📋 Features

### 🔧 Core Functionality
- **Automated Data Pipeline**: Downloads data from GCP and splits into train/test sets
- **Model Training**: LightGBM with RandomizedSearchCV for hyperparameter tuning
- **Web Prediction API**: RESTful endpoints for model inference
- **Interactive Web UI**: Modern, responsive interface for predictions
- **Health Monitoring**: Application health checks and model status

### 🏗️ Architecture Features
- **Modular Design**: Clean separation of data, model, and application layers
- **Configuration Management**: YAML-based configuration for easy deployment
- **Error Handling**: Custom exceptions and comprehensive logging
- **Scalable Structure**: Organized codebase following industry standards

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Cloud Platform account (for data storage)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hotel-reservation-prediction.git
   cd hotel-reservation-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure GCP credentials**
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   ```

5. **Set up configuration**
   ```bash
   # Update config/config.yaml with your GCP bucket details
   # Ensure all paths in config/paths_config.py are correct
   ```

### Usage

#### Training the Model
```bash
python pipeline/training_pipeline.py
```

#### Running the Web Application
```bash
python application.py
```

Visit `http://localhost:8080` to access the prediction interface.

#### Making Predictions via API
```bash
curl -X POST http://localhost:8080/ \
  -d "lead_time=30&no_of_special_request=1&avg_price_per_room=150&arrival_month=6&arrival_date=15&market_segment_type=1&no_of_week_nights=3&no_of_weekend_nights=2&type_of_meal_plan=0&room_type_reserved=1"
```

## 🏛️ Project Structure

```
hotel-reservation-prediction/
│
├── artifacts/                 # Model artifacts and data
│   ├── models/               # Trained models
│   ├── processed/            # Processed datasets
│   └── raw/                  # Raw data files
│
├── config/                   # Configuration files
│   ├── config.yaml          # Main configuration
│   ├── model_params.py      # Model hyperparameters
│   └── paths_config.py      # Path configurations
│
├── pipeline/                 # ML pipelines
│   └── training_pipeline.py # Main training pipeline
│
├── src/                      # Source code
│   ├── data_ingestion.py    # Data ingestion logic
│   ├── logger.py            # Logging utilities
│   └── custom_execption.py  # Custom exceptions
│
├── templates/                # Flask templates
│   └── index.html           # Main web interface
│
├── utils/                    # Utility functions
│   └── common_funtions.py   # Common utilities
│
├── logs/                     # Application logs
├── notebook/                 # Jupyter notebooks
├── static/                   # Static assets
├── custom_jenkins/           # Jenkins configurations
│
├── application.py            # Flask application
├── Dockerfile               # Docker configuration
├── Jenkinsfile              # Jenkins pipeline
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
└── README.md                # Project documentation
```

## 🔄 CI/CD Pipeline

The project includes a Jenkins pipeline for automated testing and deployment:

- **Automated Testing**: Unit tests and integration tests
- **Model Validation**: Performance metrics and validation checks
- **Docker Build**: Container image creation
- **Deployment**: Automated deployment to staging/production

## 📊 Model Details

### Algorithm
- **LightGBM**: Gradient boosting framework optimized for speed and accuracy
- **Hyperparameter Tuning**: RandomizedSearchCV with cross-validation
- **Evaluation Metric**: Accuracy with focus on precision/recall balance

### Features Used
- Lead time
- Number of special requests
- Average price per room
- Arrival month and date
- Market segment type
- Number of week/weekend nights
- Meal plan type
- Room type reserved

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sudhanshu**
- GitHub: [@your-github-username](https://github.com/your-github-username)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

## 🙏 Acknowledgments

- Hotel booking dataset from Kaggle
- LightGBM community for the excellent ML library
- Flask community for the web framework
- Google Cloud Platform for cloud services

---

⭐ **Star this repo if you find it useful!**

For questions or support, please open an issue on GitHub.
