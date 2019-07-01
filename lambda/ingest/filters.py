import json


def filter_github(data):
    data_dict = json.loads(data)
    if data_dict.get("repository") and data_dict["repository"].get("private"):
        return None
    return data


def filter_slack(data):
    data_dict = json.loads(data)
    if "text" in data_dict["event"]:
        del data_dict["event"]["text"]
    return json.dumps(data_dict)


"""
Map of optional filter functions for data types. Value is a function that returns a redacted
version of the data point, or None if the data point should be ignored.
"""
filter = {
    "GithubType": filter_github,
    "SlackType": filter_slack
}
