<h1 align="center" id="title">Sales Prediction Web Application</h1>

<p align="center"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0UgUiGr8hT4fVwZbsMUMwCfLhf3kOrkT1DA&amp;usqp=CAU" alt="project-image"></p>

<p id="description">Sales prediction is a critical task for businesses as it enables them to make informed decisions about inventory pricing and overall strategy. This project aims to predict item outlet sales using various machine learning techniques and a web-based application developed with Flask. We explore and compare three regression models: Linear Regression Lasso Regression and Ridge Regression to find the best-suited model for the task.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Data Preprocessing: Data Cleaning: Handling missing values and ensuring data quality. Feature Transformation: Transforming features such as normalizing numerical data and encoding categorical variables. Data Imputation: Estimating missing values for item weight and visibility.
*   Feature Engineering: Creating new features and transforming existing ones to improve model performance.
*   Linear Regression: Implementing a baseline Linear Regression model for item outlet sales prediction.
*   Lasso and Ridge Regression: Applying Lasso and Ridge Regression techniques to evaluate their performance in comparison to the baseline model. Assessing model accuracy using R2 Score and Root Mean Squared Error (RMSE).
*   Model Selection: Deciding on the most accurate model for predicting item outlet sales based on the evaluation of different techniques.
*   Web Application: Building a user-friendly web application for interacting with the predictive model. Consisting of several pages: About Page: Provides information about the project and its goals. Graph Page: Offers visualizations and insights into the dataset. Form Page: Allows users to input item and outlet details for sales prediction. Result Page: Displays the predicted item outlet sales based on user inputs.
*   Graphical Visualization: Creating visualizations to gain insights into the relationships between various factors in the dataset.
*   Model Evaluation: Providing insights into the strengths and weaknesses of each model allowing users to make informed decisions for their retail business.
*   Conclusion and Insights: Summarizing the project's findings and offering a data-driven perspective on retail business decisions.
*   User-Friendly Interface: Ensuring that the web application is easy to navigate and interact with making it accessible to users with varying levels of technical expertise.
*   Data-Driven Predictions: Enabling users to make sales predictions based on specific item and outlet characteristics.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository to your local machine:</p>

```
git clone https://github.com/yourusername/sales-prediction-web-app.git
```

<p>2. Change to the project directory:</p>

```
cd sales-prediction-web-app
```

<p>3. Create a virtual environment (optional but recommended):</p>

```
python -m venv venv source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

<p>4. Install the required packages:</p>

```
pip install -r requirements.txt
```

<p>5. Run the Flask application:</p>

```
python app.py
```

<p>6. Open your web browser and go to http://localhost:5000/ to access the application. You can use the web interface to enter item information such as Item Identifier Item Weight Item Visibility Item Fat Content Item Type Item MRP Outlet ID Outlet Establishment Year Outlet Size Outlet Location and Outlet Type. Submit the form to get a sales prediction. The application will display the predicted sales based on the entered information.</p>

<h2>🍰 Contribution Guidelines:</h2>

---

## Contribution Guidelines

Welcome to the "Predicting Item Outlet Sales" project! We appreciate your interest in contributing. To maintain a collaborative and productive environment, please follow these guidelines when contributing to the project.

### Getting Started

1. **Fork the Repository**: Start by forking the main repository to your GitHub account.

2. **Clone the Repository**: Clone your forked repository to your local development environment.

   ```bash
   git clone https://github.com/your-username/predicting-item-outlet-sales.git
   cd predicting-item-outlet-sales
   ```

3. **Create a Branch**: Create a new branch for your contribution. Make sure the branch name is descriptive and related to the issue you're addressing.

   ```bash
   git checkout -b feature/your-feature
   ```

### Making Changes

4. **Code Style**: Follow the existing code style and formatting used in the project. Consistency is key.

5. **Commits**: Make clear and concise commit messages that explain the purpose of your changes. Use present tense (e.g., "Add feature" not "Added feature").

6. **Testing**: If applicable, ensure that your code includes tests and that existing tests pass successfully. New features should be covered by appropriate tests.

7. **Documentation**: Update or create documentation if your changes affect project documentation. This includes updating README files and docstrings.

8. **Pull Request**: When your contribution is ready, push your changes to your forked repository and create a pull request (PR) to the main project repository.

### Pull Request Guidelines

9. **PR Title**: Use a descriptive title for your PR that summarizes the changes made.

10. **Description**: Provide a detailed description of your changes in the PR. Include the issue number (if applicable) and explain the rationale behind the changes.

11. **Review Requests**: If specific team members should review your PR, request reviews from them.

12. **Labels**: Apply appropriate labels to your PR to indicate its status (e.g., "enhancement," "bug," "documentation," "help wanted").

13. **Squash Commits**: If you made multiple small commits, consider squashing them into a single commit for cleaner history.

### Review and Feedback

14. **Feedback**: Be responsive to feedback provided during the review process. Address comments and concerns promptly.

15. **Revisions**: If requested changes are made, update your branch and push the changes to your PR. Notify reviewers when you're ready for re-evaluation.

### Code of Conduct

16. **Be Respectful**: Ensure respectful and professional communication. Harassment, discrimination, and rude behavior will not be tolerated.

17. **License**: By contributing to this project, you agree to license your code under the project's open-source license (if applicable).

Thank you for your contributions to the "Predicting Item Outlet Sales" project. Your efforts help make this project better and more valuable for the community.

---

Feel free to customize these guidelines to suit the specific needs and preferences of your project. Clear and comprehensive guidelines contribute to a smoother and more organized collaboration with contributors and collaborators.
  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Flask
*   Pandas
*   NumPy
*   Seaborn and Matplotlib
*   Scipy
*   Scikit-Learn (sklearn)
*   Jinja2
*   HTML and CSS
*   Linear Regression
*   Lasso and Ridge Regression

<h2>🛡️ License:</h2>

This project is licensed under the MIT License
