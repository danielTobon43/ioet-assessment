from tools.utils import parse_input_data
from tools.utils import split_chuncks
from tools.utils import factory_employee
from tools.utils import extract_day_time

week_days = set(('MO', 'TU', 'WE', 'TH', 'FR'))
weekend_days = set(('ST', 'SU'))
acme_rates = {'00:01 - 09:00': 25,
              '09:01 - 18:00' 15,
              '18:01 - 00:00' 20}

if __name__ == '__main__':
    print('ioet hello world')
    data = parse_input_data('employees_working_time.txt')
    chuncks = [split_chuncks(datetime_data, '=') for datetime_data in data]
    for chunck_data in chuncks:
        employee = factory_employee(chunck_data[0], chunck_data[1])
        for workedtime_by in employee.workingtime:
            day = workedtime_by[0]
            start_time = workedtime_by[1]
            end_time = workedtime_by[2]
            print(f'employee:{employee.name} has worked: {workedtime_by[0]}')
            if day in week_days:
                check_time_in_range(start_time, acme_rates)
