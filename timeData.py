from datetime import datetime, timedelta


def getTime(data_results):
    if data_results:
        data_split = data_results.split('o ')
        if len(data_split) > 1:
            leftWords = data_split[0].strip()
            timeString = data_split[1].strip()
            try:
                current_time = datetime.strptime(timeString, "%H:%M")
                add_hour = current_time + timedelta(hours=1)

                # Convert add_hour back to string
                add_hour_str = add_hour.strftime("%H:%M")


                # Concatenate leftWords and add_hour_str
                data_results = f"{leftWords} o {add_hour_str}"


            except ValueError as e:
                print(f"Error parsing timeString: {timeString}")
                print(e)
    return data_results
def getCurrentTime():
    current_time = datetime.now()
    return current_time

def getOfferTime(data_results):
    if data_results:
        data_split = data_results.split('o ')
        if len(data_split) > 1:
            timeString = data_split[1].strip()
            try:
                current_time = datetime.strptime(timeString, "%H:%M")
                add_hour = current_time + timedelta(hours=1)
                data_results = add_hour
            except ValueError as e:

                print(e)
    return data_results
