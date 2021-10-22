import datetime

from services import scrapper_service, db_service
from utils import constants
from views import info_view


def _validate_date(date: str):
    """

    :param date:
    :return:
    """
    try:
        datetime.datetime.strptime(date, constants.DATE_FORMAT)
        return True
    except ValueError:
        return False


def _fetch_covid_info_from_db(date: str, is_date_valid: bool):
    """
    Fetch Covid-19 info from database
    :param is_date_valid:
    :param date:
    :return:
    """

    # Always returns the latest result if date parameter is invalid
    if date == "latest" or is_date_valid is False:
        covid_info = db_service.get_latest_covid_info()
        today = datetime.datetime.today().now().strftime(constants.DATE_FORMAT)

        if covid_info.get("lastPostedDate", "") != today:
            covid_info = {}
    else:
        covid_info = db_service.get_covid_info_by_date(date)

    return covid_info


def _create_response(key: str, covid_info: dict):
    """

    :param key:
    :param covid_info:
    :return:
    """

    if key == "info":
        return covid_info

    for k in list(covid_info["data"].keys()):
        if k != key:
            covid_info["data"].pop(k)

    return covid_info


def get_covid_info(key: str, date: str):
    """

    :param key:
    :param date:
    :return:
    """

    is_date_valid = _validate_date(date)

    # Fetch Covid-19 information from database
    covid_info = _fetch_covid_info_from_db(date, is_date_valid)

    if not covid_info:
        formatted_date = ""

        if is_date_valid:
            formatted_date = datetime.datetime.strptime(date, constants.DATE_FORMAT) \
                .strftime('%A-%B-%d-%Y').lower().replace("-0", "-")

        covid_info_data = scrapper_service.get_covid_info(formatted_date)
        covid_info = info_view.map_data(covid_info_data)

        # Update database with scrapped Covid-19 info
        db_service.insert_covid_info(covid_info)

    covid_stats_response = _create_response(key, covid_info)

    return covid_stats_response
