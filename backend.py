import requests

API_Key = "0660e01b8a5c38ff695c856bf12b36c1"


def get_data(place,forecast_days=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()
    filterd_data = data["list"]
    nr_values = 8*forecast_days
    filterd_data = filterd_data[:nr_values]
    return filterd_data


if __name__ =="__main__":
    print(get_data(place="Tokyo",forecast_days=3))