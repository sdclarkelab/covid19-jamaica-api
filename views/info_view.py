def _extract_date_range_data(key: str, data: dict):
    """

    :param key:
    :param data:
    :return:
    """
    values = data.get(key, [])

    return {
        "24Hours": values[0] if len(values) > 0 else "",
        "overall": values[1] if len(values) > 0 else "",
    }


def _extract_covid_testing_data(key: str, data: dict):
    """

    :param key:
    :param data:
    :return:
    """
    return {
        "pcr": data.get(key, '')[0],
        "publicAntigen": data.get(key, '')[1],
        "privateAntigen": data.get(key, '')[2],
        "total": data.get(key, '')[3]
    }


def map_data(data: dict):
    """

    :param data:
    :return:
    """
    return {
        "data": {
            "newCases": {
                "confirmedCases": _extract_date_range_data(key="Confirmed Cases", data=data)
            },
            "sexClassification": {
                "males": _extract_date_range_data(key="Males", data=data),
                "females": _extract_date_range_data(key="Females", data=data),
                "underInvestigation": _extract_date_range_data(key="Under Investigation", data=data)
            },
            "ageRange": _extract_date_range_data(key="AGE RANGE", data=data),
            "parishClassification": {
                "ksa": _extract_date_range_data(key="Kingston & St. Andrew", data=data),
                "clarendon": _extract_date_range_data(key="Clarendon", data=data),
                "stCatherine": _extract_date_range_data(key="St. Catherine", data=data),
                "stJames": _extract_date_range_data(key="St. James", data=data),
                "hanover": _extract_date_range_data(key="Hanover", data=data),
                "portland": _extract_date_range_data(key="Portland", data=data),
                "stMary": _extract_date_range_data(key="St. Mary", data=data),
                "trelawny": _extract_date_range_data(key="Trelawny", data=data),
                "stAnn": _extract_date_range_data(key="St. Ann", data=data),
                "manchester": _extract_date_range_data(key="Manchester", data=data),
                "stElizabeth": _extract_date_range_data(key="St. Elizabeth", data=data),
                "stThomas": _extract_date_range_data(key="St. Thomas", data=data),
                "westmoreland": _extract_date_range_data(key="Westmoreland", data=data),
            },
            "covidTesting": {
                "positivesToday": _extract_covid_testing_data(key="POSITIVES Today", data=data),
                "cumulativePositives": _extract_covid_testing_data(key="Cumulative POSITIVES", data=data),
                "negativeToday": _extract_covid_testing_data(key="NEGATIVE today", data=data),
                "cumulativeNegatives": _extract_covid_testing_data(key="Cumulative NEGATIVES", data=data),
                "totalTestsToday": _extract_covid_testing_data(key="TOTAL TESTS TODAY", data=data),
                "totalTestCumulative": _extract_covid_testing_data(key="TOTAL TESTS CUMULATIVE", data=data)
            },
            "deaths": {
                "deathCount": _extract_date_range_data(key="Deaths", data=data),
                "coincidentalDeaths": _extract_date_range_data(key="Coincidental Deaths", data=data),
                "deathsUnderInvestigation": _extract_date_range_data(key="Deaths under investigation", data=data)
            },
            "recoveries": {
                "recovered": _extract_date_range_data(key="Recovered", data=data),
                "active": _extract_date_range_data(key="Active Cases", data=data)
            },
            "quarantine": {
                "inFacility": _extract_date_range_data(key="Number in Facility Quarantine", data=data),
                "inHome": _extract_date_range_data(key="Number in Home Quarantine", data=data)
            },
            "hospitalManagement": {
                "numbHospitalized": _extract_date_range_data(key="Number Hospitalised", data=data),
                "patients": {
                    "moderately": _extract_date_range_data(key="Patients Moderately Ill", data=data),
                    "severely": _extract_date_range_data(key="Patients Severely Ill", data=data),
                    "critical": _extract_date_range_data(key="Patients Critically Ill", data=data)
                }
            },
            "nonHospitalIsolation": {
                "stepDownFacility": _extract_date_range_data(key="Step Down Facilities", data=data),
                "stateFacility": _extract_date_range_data(key="State Facilities", data=data),
                "home": _extract_date_range_data(key="Home", data=data)
            },
            "transmissionStatus": {
                "contactOfConfirmedCase": _extract_date_range_data(key="Contact of a Confirmed Case", data=data),
                "imported": _extract_date_range_data(key="Imported", data=data),
                "localTransmission": _extract_date_range_data(key="Local Transmission (Not Epi Linked)", data=data),
                "underInvestigation": _extract_date_range_data(key="Under Investigation Trans", data=data),
                "workplace": _extract_date_range_data(key="Workplace Cluster", data=data)
            }
        },
        "lastRefreshed": data["lastRefreshed"],
        "lastPostedDate": data["lastPostedDate"],
        "infoDate": data["infoDate"]
    }
