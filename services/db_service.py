from tinydb import TinyDB, Query

DB = TinyDB('database/covid19_jam_info.json')


def get_covid_info_by_date(date: str):
    """

    :param date:
    :return:
    """
    stats_query = Query()

    # Gets list of result
    results = DB.search(stats_query.infoDate == date)
    return results[0] if len(results) > 0 else results


def get_latest_covid_info():
    """

    :return:
    """
    db_results = DB.all()
    if len(db_results):
        return sorted(db_results, key=lambda d: d['infoDate'], reverse=True)[0]

    return {}


def insert_covid_info(covid_info):
    DB.insert(covid_info)
