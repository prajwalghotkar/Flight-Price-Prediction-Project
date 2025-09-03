# Flight Price Prediction Project
##### Overview
- This project aims to predict flight ticket prices based on various input features using machine learning techniques. The workflow includes data preparation, model building, choosing the best predictive model, and deploying the machine learning model as a web application using Flask. This enables users to get live flight price predictions through a user-friendly interface.
---
##### Features
- Data preprocessing and model selection for accurate flight price prediction
- Multiple machine learning model evaluations to select the best one
- Deployment of predictive model via Flask for real-time predictions
- Simple web interface for users to input flight details and get price estimates
- Deployment-ready with integration to platforms like Heroku
---

##### Steps
- **Choose your use-case:** Define the specific prediction scenario you are targeting.
- **Prepare your dataset:** Clean and preprocess the flight data for model training.
- **Build and select models:** Train machine learning algorithms and choose the best-performing model.
- **Create a web app using Flask:** Build the frontend and backend for user interaction.
- **Commit your code to GitHub:** Maintain version control and code sharing.
- **Create a Heroku account:** Set up cloud platform account for deployment.
- **Link GitHub and Heroku:** Integrate GitHub repository with Heroku for continuous deployment.
- **Deploy and test your app:** Launch the app and verify its functionality in a live environment.
---
##### Installation

###### Step 1) Install Flask Cors through Jupyter Notebook
- pip install flask_cors
![image](https://github.com/user-attachments/assets/64d23b10-0dc8-4381-8859-319d764fdb79)

###### Step 2) Create a folder and keep the file as specified
![praajwal](https://github.com/user-attachments/assets/f153cc3f-afa5-4393-ab71-6fd4801f11a4)

###### Step 3) Open Pycharm
![image](https://github.com/user-attachments/assets/89c317f4-b331-4d64-9922-e7c485cb3512)
###### Select the Folder which you created

###### Step 4) Right Click Build.py then Run, This create the model then generate a new pickle file in the same folder
![Screenshot 2025-02-06 164232](https://github.com/user-attachments/assets/9b470d67-48c5-40b5-b663-888e90a33ea6)

###### Pickle File
![praajwal](https://github.com/user-attachments/assets/712260db-d146-427b-90bd-7f35f7ededc6)

###### Step 5) Right click and Run app.py
![Screenshot 2025-02-06 162814](https://github.com/user-attachments/assets/3f7e5f15-0365-45c6-a031-04f5a3be7443)

###### Step 6) Copy this URL and open in the Browser
![Screenshot 2025-02-06 162912](https://github.com/user-attachments/assets/f6a2d4bd-21b4-4296-bef2-5de1e82dff47)
<img width="1920" height="960" alt="flight" src="https://github.com/user-attachments/assets/2d855fd3-4b22-4f8b-b234-823ba39a5bbb" />
---

##### Usage
- Open the URL provided by Flask or deployed Heroku app in your web browser.
- Input the required flight details.
- Click submit to receive a predicted flight price
---

##### File Structure
- build.py — Script for data preparation, model building, training, and generating the serialized model.
- app.py — Flask backend for serving web API and rendering frontend.
- Dataset files — Flight data CSV for training.
- Frontend files (HTML, CSS) for user interface.

---

##### Technologies Used
- Python
- Pandas, NumPy (Data Manipulation)
- Scikit-learn (Machine Learning)
- Flask, Flask-Cors (Web Framework)
- Heroku (Cloud Deployment)
- HTML, CSS (Frontend)

---
##### Future Benefits
- **User Convenience**: Provides instant, data-driven flight price estimates to travelers and travel agents.
- **Cost Optimization:** Airlines and travel platforms can use insights predicted to optimize pricing strategies.
- **Scalability:** Model and deployment pipeline support expansion to additional routes, airlines, and international datasets.
- **Continuous Improvement:** Ability to retrain the model with new data for enhanced predictive performance over time.
- **Business Integration:** Possibility to integrate with flight booking platforms and travel agencies for dynamic pricing tools.

##### https://vercel.com/prajwals-projects-76a77902/flight-price-prediction-project
---
by Prajwal 


