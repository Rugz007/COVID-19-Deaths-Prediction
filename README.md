# COVID-19 Vaccinations Effects on Deaths Prediction

This repository contains code and resources for predicting the effects of COVID-19 vaccinations on deaths caused by the virus. The goal is to analyze the impact of vaccinations on reducing mortality rates and provide insights into the effectiveness of different vaccination strategies.

## Technologies Used

- Python: The main programming language used for data analysis, modeling, and visualization.
- Machine Learning Libraries: Various machine learning libraries such as scikit-learn, TensorFlow, and PyTorch are utilized for building predictive models.
- Data Analysis Libraries: Pandas and NumPy are used for data manipulation and analysis.
- Data Visualization: Matplotlib and Seaborn are employed for visualizing the data and model outputs.
- Docker: The project is dockerized to ensure easy deployment and reproducibility.

## Running the project

This project is dockerized to simplify the setup process and ensure consistent environments across different systems. To run the project using Docker, follow these steps:

1. Install Docker on your machine.
2. Build the Docker image: `docker pull rugz007/covid19.`
3. Run the Docker container: `docker run -d --name mycontainer -p 80:80 covid19`
4. Open your browser and go to `localhost:80/docs` to view the API.
5. Click on "Try it out" and paste one of the test JSONs present which are made to help you with the input format.
6. Click on "Execute" and you will get the results.

## Docker Image
The docker image can be found at [Docker Hub](https://hub.docker.com/repository/docker/rugz007/covid19).

## Data
The data is obtained from [CDC Covid Vaccination Data](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh/about_data) amd [John Hopkins Covid 19 Data](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh/about_data). 

## Output
We have attached two PDFs, Interactions.pdf and Visualizations.pdf, which contain the interactions with GPT and visualizations of the data respectively.

## License
This project is licensed under the MIT License.
