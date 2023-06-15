def laptime_to_ms(laptime):
    minutes = int(laptime[0])
    seconds = int(laptime[2:4])
    milliseconds = int(laptime[5:8])
    return (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

def ms_to_laptime(milliseconds):
    minutes = int(milliseconds / (60 * 1000))
    seconds = int((milliseconds % (60 * 1000)) / 1000)
    milliseconds = int(milliseconds % 1000)
    return f"{minutes:02}:{seconds:02}.{milliseconds:03}"

def ms_to_seconds(ms):
    return ms / 1000

def lap_time_to_seconds(lap_time_string):
    minutes, seconds = lap_time_string.split(':')
    seconds, milliseconds = seconds.split('.')
    total_seconds = float(minutes) * 60 + float(seconds) + float(milliseconds) / 1000
    return total_seconds

def seconds_to_lap_time(total_seconds):
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    lap_time_string = '{:02d}:{:02d}.{:03d}'.format(minutes, seconds, milliseconds)
    return lap_time_string

def get_index(name, lst):
    for i in range(len(lst)):
        if lst[i][0].lower() == name.lower():
            return i
    return None
