import datetime
import random
import re
import time

import requests
from bs4 import BeautifulSoup

from utils import constants


def _get_random_ua():
    """

    :return:
    """
    random_ua = ''
    try:
        random_ua = random.choice(constants.USER_AGENTS)
    except Exception as e:
        print(e)
    finally:
        return random_ua


def _get_soup(url: str, timeout_retry_count: int = 2):
    """

    :param url:
    :param timeout_retry_count:
    :return:
    """

    soup = None
    headers = {
        'User-Agent': _get_random_ua(),
        'Referer': 'https://www.google.com/',
    }

    for i in range(0, timeout_retry_count):
        response = requests.get(url, headers=headers)
        status_code = response.status_code

        if status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            break

        delay = random.choice([7, 4, 6, 2, 10, 19])
        time.sleep(delay)

    return soup


def _get_latest_clinical_summary_url():
    """

    :return:
    """
    url = "https://www.moh.gov.jm/updates/coronavirus/covid-19-clinical-management-summary/"
    soup = _get_soup(url)
    links = soup.find_all("a", {"class": "read-more btn btn-default hvr-grow"})

    return links[0]['href']


def _get_clinical_summary_data(url):
    """

    :param url:
    :return:
    """
    soup = _get_soup(url)

    data = {}
    key = ""
    values = []

    p = re.compile(r'-for-(.*)/')
    day_of_the_week = str(p.search(url).group(1))

    if soup:
        data["infoDate"] = datetime.datetime.strptime(day_of_the_week.title(), '%A-%B-%d-%Y') \
            .strftime(constants.DATE_FORMAT).lower()

        data["lastRefreshed"] = datetime.datetime.today().strftime(constants.DATE_FORMAT)

        soup_datetime = soup.find_all("time", {"class": "entry-date published updated"})[0]["datetime"]
        data["lastPostedDate"] = datetime.datetime.strptime(soup_datetime, '%Y-%m-%dT%H:%M:%S%z') \
            .strftime(constants.DATE_FORMAT).lower()

        for tr in soup.find_all("tr"):
            for index, td in enumerate(tr.find_all("td")):
                td_text = td.text.strip()

                if index == 0:
                    key = td_text
                else:
                    values.append(td_text)

            if key == "Under Investigation" and key in data.keys():
                key = key + " Trans"

            # TODO: Implement solution to read rowspan value
            if key == "Cumulative NEGATIVES":
                values.insert(1, data["NEGATIVE today"][1])

            data[key] = values
            values = []
            key = ""

    return data


def get_covid_info(date: str):
    """

    :param date:
    :return:
    """

    url = f'https://www.moh.gov.jm/covid-19-clinical-management-summary-for-{date}/' if date else \
        _get_latest_clinical_summary_url()

    return _get_clinical_summary_data(url)
