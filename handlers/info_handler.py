from services import info_service


def get_info(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("info", date)


def get_new_cases(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("newCases", date)


def get_sex_classification(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("sexClassification", date)


def get_age_range(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("ageRange", date)


def get_parish_classification(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("parishClassification", date)


def get_covid_testing(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("parishClassification", date)


def get_deaths(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("deaths", date)


def get_recoveries(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("recoveries", date)


def get_quarantine(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("quarantine", date)


def get_hospital_management(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("hospitalManagement", date)


def get_non_hospital_isolation(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("nonHospitalIsolation", date)


def get_transmission_status(date: str):
    """

    :param date:
    :return:
    """
    return info_service.get_covid_info("transmissionStatus", date)
