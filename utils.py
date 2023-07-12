import numpy as np
import pickle
import config


class StudentInfo():
    def __init__(self, Age, Gender, Stream, Internships, CGPA, Hostel, HistoryOfBacklogs):
        self.Age = Age
        self.Gender = Gender
        self.Stream = Stream
        self.Internships = Internships
        self.CGPA = CGPA
        self.Hostel = Hostel
        self.HistoryOfBacklogs = HistoryOfBacklogs

    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

    def predict_placement(self):
        self.load_model()

        # Define the mappings
        gender_data = {'male': 1, 'female': 0}
        stream_data = {
            'Electronics And Communication': 0,
            'Computer Science': 1,
            'Information Technology': 2,
            'Mechanical': 3,
            'Electrical': 4,
            'Civil': 5
        }

        # Convert the values
        Gender = gender_data[self.Gender]
        Stream = stream_data[self.Stream]

        # Create the test array
        test_array = np.array([self.Age, Gender, Stream, self.Internships, self.CGPA, self.Hostel, self.HistoryOfBacklogs])

        # Make a prediction
        prediction = self.model.predict([test_array])

        return prediction