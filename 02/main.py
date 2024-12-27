def read_file(file_path: str) -> list:
    reports_list = []
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.split(' ')
            reports_list.append(line)
    return reports_list

def validate_reports(reports_list: list) -> int:
    unsafe_reports = []
    detailed_logging = True
    print("Validating reports")
    print("Number of reports:",len(reports_list))
    total_increasing_reports = 0
    total_decreasing_reports = 0
    total_valid_reports = 0
    total_non_gradual_reports = 0
    for report in reports_list:
        # print("Report:")
        # print(report)
        report_safe = False
        increasing = 0
        decreasing = 0
        non_gradual_steps = 0
        for level in range(len(report) - 1):
            current_level = int(report[level])
            next_level = int(report[level + 1])
            level_delta = abs(abs(current_level) - abs(next_level))
            if detailed_logging:
                print("Current:",current_level,"Next:", next_level,"Delta:",level_delta)
            if 1 <= level_delta <= 3:
                if (current_level < next_level) and (decreasing == 0):
                    increasing += 1
                    if detailed_logging:
                        print("Increasing",increasing)
                elif current_level < next_level and (decreasing != 0):
                    increasing += 1
                    if detailed_logging:
                        print("Error, change in direction found")
                elif current_level > next_level and (increasing == 0):
                    decreasing += 1
                    if detailed_logging:
                        print("Decreasing",decreasing)
                elif current_level > next_level & (increasing != 0):
                    decreasing += 1
                    print("Error, change in direction found")
            elif level_delta < 1 or level_delta > 3:
                non_gradual_steps += 1
        # print("Final: Increasing:", increasing,"Decreasing:",decreasing,"Non gradual steps:",non_gradual_steps)
        if non_gradual_steps == 0:
            if detailed_logging:
                print("Valid gradient")
            if increasing > 0 & decreasing == 0:
                total_increasing_reports +=1
            if decreasing > 0 & increasing == 0:
                total_decreasing_reports +=1
            if abs((increasing - decreasing)/(increasing + decreasing)) == 1:
                print("Singular direction", report)
                total_valid_reports += 1
                report_safe = True
            else:
                unsafe_reports.append(report)
        elif non_gradual_steps != 0:
            print("Non gradual:",report)
            unsafe_reports.append(report)
            total_non_gradual_reports += 1
        # while report_safe != True:

    print("Number of reports:",len(reports_list))
    print("Total non-gradual reports:",total_non_gradual_reports)
    print("Total decreasing:",total_decreasing_reports)
    print("Total increasing:",total_increasing_reports)
    print("Unsafe reports:",len(unsafe_reports))
    return total_valid_reports, unsafe_reports

def validate_reports_with_tolerance(reports_list: list) -> int:
    detailed_logging = True
    total_increasing_reports = 0
    total_decreasing_reports = 0
    total_valid_reports = 0
    total_non_gradual_reports = 0
    for report in reports_list:
        working_reports = [report[:] for report_level in report]
        print("Working reports length:",len(working_reports))
        print("Working reports:",working_reports)
        report_safe = False
        increasing = 0
        decreasing = 0
        non_gradual_steps = 0
        for working_report in range(0,len(working_reports)):
            if report_safe != True:
                print("Report safety is:",report_safe)
                active_report = working_reports[working_report]
                print("Report index before:",working_report)
                if working_report > 0:
                    print("Report index after:",working_report)
                    print("Active report is:",active_report)
                    active_report.pop(working_report)
                    print("active report after pop",active_report)
                print("Report is:")
                print(active_report)
                # working_report = working_report.pop(working_report[working_report])
                print("Report safety after check:",report_safe)
                increasing = 0
                decreasing = 0
                non_gradual_steps = 0
                for level in range(len(active_report) - 1):
                    print("Active report inside level loop:",active_report)
                    if report_safe != True:
                        current_level = int(active_report[level])
                        next_level = int(active_report[level + 1])
                        level_delta = abs(abs(current_level) - abs(next_level))
                        if detailed_logging:
                            print("Current:",current_level,"Next:", next_level,"Delta:",level_delta)
                        if 1 <= level_delta <= 3:
                            if (current_level < next_level) and (decreasing == 0):
                                increasing += 1
                                if detailed_logging:
                                    print("Increasing",increasing)
                            elif current_level < next_level and (decreasing != 0):
                                increasing += 1
                                if detailed_logging:
                                    print("Error, change in direction found")
                            elif current_level > next_level and (increasing == 0):
                                decreasing += 1
                                if detailed_logging:
                                    print("Decreasing",decreasing)
                            elif current_level > next_level & (increasing != 0):
                                decreasing += 1
                                print("Error, change in direction found")
                        elif level_delta < 1 or level_delta > 3:
                            non_gradual_steps += 1
                if non_gradual_steps == 0 and report_safe == False:
                    if detailed_logging:
                        print("Valid gradient")
                    if increasing > 0 & decreasing == 0:
                        total_increasing_reports +=1
                    if decreasing > 0 & increasing == 0:
                        total_decreasing_reports +=1
                    if abs((increasing - decreasing)/(increasing + decreasing)) == 1:
                        total_valid_reports += 1
                        report_safe = True
                        print("Singular direction", active_report, "Total valid reports:",total_valid_reports)
                elif non_gradual_steps != 0:
                    print("Non gradual:",active_report)
                    total_non_gradual_reports += 1
                # while report_safe != True:
            else:
                print("Report is safe, no change mode:",report_safe, "(",total_valid_reports,")")

    print("Number of reports with tolerance:",len(reports_list))
    print("Total non-gradual reports with tolerance:",total_non_gradual_reports)
    print("Total decreasing with tolerance:",total_decreasing_reports)
    print("Total increasing with tolerance:",total_increasing_reports)
    return total_valid_reports

def validate_unsafe_reports(reports_list: list) -> int:
    detailed_logging = True
    total_increasing_reports = 0
    total_decreasing_reports = 0
    total_valid_reports = 0
    total_non_gradual_reports = 0
    for report in reports_list:
        working_reports = [report[:] for report_level in report]
        print("Working reports length:",len(working_reports))
        print("Working reports:",working_reports)
        report_safe = False
        increasing = 0
        decreasing = 0
        non_gradual_steps = 0
        for working_report in range(0,len(working_reports)):
            if report_safe != True:
                print("Report safety is:",report_safe)
                active_report = working_reports[working_report]
                print("Report index after:",working_report)
                print("Active report is:",active_report)
                active_report.pop(working_report)
                print("active report after pop",active_report)
                print("Report is:")
                print(active_report)
                # working_report = working_report.pop(working_report[working_report])
                print("Report safety after check:",report_safe)
                increasing = 0
                decreasing = 0
                non_gradual_steps = 0
                for level in range(len(active_report) - 1):
                    print("Active report inside level loop:",active_report)
                    if report_safe != True:
                        current_level = int(active_report[level])
                        next_level = int(active_report[level + 1])
                        level_delta = abs(abs(current_level) - abs(next_level))
                        if detailed_logging:
                            print("Current:",current_level,"Next:", next_level,"Delta:",level_delta)
                        if 1 <= level_delta <= 3:
                            if (current_level < next_level) and (decreasing == 0):
                                increasing += 1
                                if detailed_logging:
                                    print("Increasing",increasing)
                            elif current_level < next_level and (decreasing != 0):
                                increasing += 1
                                if detailed_logging:
                                    print("Error, change in direction found")
                            elif current_level > next_level and (increasing == 0):
                                decreasing += 1
                                if detailed_logging:
                                    print("Decreasing",decreasing)
                            elif current_level > next_level & (increasing != 0):
                                decreasing += 1
                                print("Error, change in direction found")
                        elif level_delta < 1 or level_delta > 3:
                            non_gradual_steps += 1
                if non_gradual_steps == 0 and report_safe == False:
                    if detailed_logging:
                        print("Valid gradient")
                    if increasing > 0 & decreasing == 0:
                        total_increasing_reports +=1
                    if decreasing > 0 & increasing == 0:
                        total_decreasing_reports +=1
                    if abs((increasing - decreasing)/(increasing + decreasing)) == 1:
                        total_valid_reports += 1
                        report_safe = True
                        print("Singular direction", active_report, "Total valid reports:",total_valid_reports)
                elif non_gradual_steps != 0:
                    print("Non gradual:",active_report)
                    total_non_gradual_reports += 1
                # while report_safe != True:
            else:
                print("Report is safe, no change mode:",report_safe, "(",total_valid_reports,")")

    print("Number of reports:",len(reports_list))
    print("Total non-gradual reports:",total_non_gradual_reports)
    print("Total decreasing:",total_decreasing_reports)
    print("Total increasing:",total_increasing_reports)
    return total_valid_reports

reports = read_file('./input.txt')
unsafe_reports_output = read_file('unsafe_input.txt')
total_valid_reports, unsafe_reports = validate_reports(reports)
# print("Total valid reports with tolerance:",validate_reports_with_tolerance(reports))
print("Total safe reports:",total_valid_reports)
total_validated_unsafe_reports = validate_unsafe_reports(unsafe_reports_output)
print("Total safe reports with dampener:",total_valid_reports + total_validated_unsafe_reports)
# with open('unsafe_input.txt', 'w') as file:
#     for sublist in unsafe_reports:
#         # Join all items in the sublist into a single string with a comma separator
#         # Strip any newlines in the last element and add a newline after each sublist
#         line = ' '.join(item.strip() for item in sublist) + '\n'
#         # Write the line to the file
#         file.write(line)