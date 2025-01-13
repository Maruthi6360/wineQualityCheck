# Wine Quality Prediction Project

This project is focused on predicting the quality of wine based on various chemical properties using machine learning techniques. The project utilizes a dataset of red wine samples, applying data preprocessing, feature selection, and model training to achieve accurate predictions.

## Dataset

The dataset used in this project is sourced from the UCI Machine Learning Repository and contains information on the physicochemical attributes and quality ratings of red wine samples from the Vinho Verde region of Portugal.

- **Red Wine:** 1,599 samples


### Attributes

The dataset includes the following chemical properties:

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (score between 0 and 10)

## Project Structure

The repository contains the following key files:

- `wineQuality.ipynb`: Jupyter Notebook containing the complete analysis, data preprocessing, model training, and evaluation.
- `data/`: Directory containing the wine quality dataset (CSV files).
- `README.md`: This file providing an overview of the project.

## Installation

To run this project, ensure you have Python installed along with the necessary libraries. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Maruthi6360/wine-quality-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd wine-quality-prediction
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook wineQuality.ipynb
   ```
4. Follow the steps in the notebook to explore the data, preprocess it, and train machine learning models for wine quality prediction.

## Models Used

- Linear Regression


## Evaluation Metrics

The models are evaluated using the following metrics:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R^2) score
- Accuracy (for classification models)

## Results

The final model achieved a high accuracy in predicting the quality of  red wines. Detailed results and comparisons are available in the notebook.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## Contact

For any inquiries or issues, please contact [vmaruthi6360@gmail.com].

