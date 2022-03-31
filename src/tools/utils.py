from .employee import Employee


def parse_input_data(path):
    with open(path) as f:
        employees = f.readlines()
        return employees


def split_chuncks(datetime_data, separator):
    chuncks = datetime_data.split(separator)
    return chuncks


def rawtime_to_standard(rawtime):
    standard_rawtime = rawtime.strip().upper()
    return standard_rawtime


def factory_employee(name, rawtime):
    employee = Employee(name, rawtime_to_standard(rawtime))
    chunckstime = [extract_day_time(timedata) for timedata in split_chuncks(employee.rawtime, ',')]
    employee.workingtime = chunckstime
    return employee


def extract_day_time(chunck_time):
    day = chunck_time[0:2]
    start_time = chunck_time[2:7]
    end_time = chunck_time[8::]
    # print(f'day: {day} s_time:{start_time} e_time:{end_time}')
    return (day, start_time, end_time)


def check_time_in_range(current_time, acme_rates):
    for rate_time in ['00:01', '09:01', '18:01']:
        if current_time >= rate_time:
            return acme_rates[rate_time]
