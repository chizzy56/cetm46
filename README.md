## Website Legitimacy Checker
The Website Legitimacy Checker is a web application designed to help users identify whether websites are legitimate or potential phishing threats. This application leverages the power of machine learning with a Random Forest Classifier, analyzing various website characteristics to make predictions.
Visit: https://chioma.streamlit.app/   for the deployed app.

## Features
### Interactive Predictions: Input features of a website to get real-time predictions on its legitimacy.
### Streamlit Integration: User-friendly web interface built with Streamlit.
### Data Caching: Enhanced performance through Streamlit's caching mechanisms.
## Getting Started
## Prerequisites
Before you can run this application, you'll need to install Python and several libraries. The project is built using Python 3.8 or newer.

## Installation
Clone the repository:


git clone https://github.com/chizzy56/cetm46.git 
Navigate to the project directory:

cd website-legitimacy-checker
Install required Python packages:
pip install -r requirements.txt
## Running the Application
Run the application using Streamlit:

arduino
streamlit run app.py
Navigate to http://localhost:8501 in your web browser to view the app.

## Usage
The application includes several pages:

## Home: Introduction and general information about the app.
## Legitimacy Checker: Where users can enter website features and receive a legitimacy prediction.
## About: Information on how the application works and the model behind it.
Input the required website features into the legitimacy checker page to get a prediction. The model uses features such as Google Index, Page Rank, Web Traffic, Number of Hyperlinks, and URL Length.

## How It Works
This application uses a Random Forest Classifier trained on historical data to predict website legitimacy. The load_data() function reads data from a CSV file, and the model is trained on the selected features. Predictions are made based on user input received via the web interface.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit pull requests with any enhancements. You can also open issues for bugs or new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Visit: https://chioma.streamlit.app/   for the deployed app.
