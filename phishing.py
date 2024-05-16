import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv('C:/Users/MD/Downloads/data_new.csv')  # Replace with the actual path to your data file
    return data

data = load_data()

# Define the selected features
selected_features = ['google_index', 'page_rank', 'web_traffic', 'nb_hyperlinks', 'length_url']

# Extract features and target variable
X = data[selected_features]
y = data['status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a random forest model
random_forest = RandomForestClassifier()

# Train the model
random_forest.fit(X_train, y_train)

def predict_website_legitimacy(features):
    prediction = random_forest.predict([features])
    return prediction[0]

def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox('Select a page:', ['Home', 'Legitimacy Checker', 'About'])

    if page == 'Home':
        st.title('Welcome to the Website Legitimacy Checker')
        st.image('C:/Users/MD/Downloads/krakenimages-376KN_ISplE-unsplash.jpg')
        st.write('This application helps you to determine if a website is legitimate or a phishing website.')
        st.write('Use the sidebar to navigate to different sections of the app.')
    
    elif page == 'Legitimacy Checker':
        st.title('Website Legitimacy Checker')
        
        # User input for features
        st.write('Please enter the following features of the website:')
        google_index = st.slider('Google Index', min_value=0, max_value=1)
        page_rank = st.slider('Page Rank', min_value=0, max_value=10)
        web_traffic = st.slider('Web Traffic', min_value=0, max_value=100)
        nb_hyperlinks = st.slider('Number of Hyperlinks', min_value=0, max_value=1000)
        length_url = st.slider('Length of URL', min_value=0, max_value=100)

        features = [google_index, page_rank, web_traffic, nb_hyperlinks, length_url]

        if st.button('Check Legitimacy'):
            # Predict website legitimacy
            prediction = predict_website_legitimacy(features)
            if prediction == 0:
                st.success('This website is legitimate.')
                st.image('C:/Users/MD/Downloads/christina-wocintechchat-com-KAULAzQwxzE-unsplash.jpg')
            else:
                st.error('This website is a phishing website.')
                st.image('C:/Users/MD/Downloads/matt-artz-YPd84QSltZ8-unsplash.jpg')

    elif page == 'About':
        st.title('About')
        st.image('C:/Users/MD/Downloads/jason-goodman-vbxyFxlgpjM-unsplash.jpg')
        st.write('This application uses a Random Forest Classifier to predict the legitimacy of a website based on various features.')
        st.write('It was developed to help users identify potentially harmful websites.')

if __name__ == "__main__":
    main()
