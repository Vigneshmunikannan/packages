def calculate_grade(score):
    if score is None:
         return "Score must not be None"
    elif not isinstance(score, (int, float)):
            raise TypeError("Input must be number")
    elif 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif score < 0:
        raise ValueError("Mark must be grater than or equal to 0")
    else:
        return 'F'