from sklearn.tree import DecisionTreeClassifier


class AdaptivePreferenceModel:
    """
    Machine-learning component for predicting a user's
    preferred interface style from interaction history.
    """

    def __init__(self):
        # Initial training examples represent different
        # interaction patterns.
        self.training_data = [
            [5, 1, 1],
            [4, 2, 1],
            [6, 1, 0],

            [1, 5, 1],
            [2, 4, 1],
            [1, 6, 0],

            [1, 1, 5],
            [1, 2, 4],
            [0, 1, 6]
        ]

        self.training_labels = [
            "simple",
            "simple",
            "simple",

            "detailed",
            "detailed",
            "detailed",

            "dark",
            "dark",
            "dark"
        ]

        self.model = DecisionTreeClassifier(
            random_state=42,
            max_depth=3
        )

        self.model.fit(
            self.training_data,
            self.training_labels
        )

    def predict_preference(self, simple_count, detailed_count, dark_count):
        """
        Predict the user's preferred interface based
        on their interaction history.
        """

        features = [[
            simple_count,
            detailed_count,
            dark_count
        ]]

        prediction = self.model.predict(features)

        return prediction[0]