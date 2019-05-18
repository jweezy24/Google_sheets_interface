import google_utils.retrieve_responses as getter


def load_data():
    data = getter.get_all()
    return data
