"""
datatime needed for current time.
sqlite3 as DB.
time for time.sleep().
requests for doing HTTP GET requests.
"""
from datetime import datetime
import sqlite3
import time
import requests


def create_table():
    """
    Creates a table that will be used for storing geoip data.
    """
    conn = sqlite3.connect("db/geoip.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS geoip_info (
                       timestamp TEXT,
                       ip TEXT,
                       status INTEGER,
                       delay TEXT,
                       credit TEXT,
                       city TEXT,
                       region TEXT,
                       regionCode TEXT,
                       regionName TEXT,
                       areaCode TEXT,
                       dmaCode TEXT,
                       countryCode TEXT,
                       countryName TEXT,
                       inEU INTEGER,
                       euVATrate INTEGER,
                       continentCode TEXT,
                       continentName TEXT,
                       latitude TEXT,
                       longitude TEXT,
                       locationAccuracyRadius TEXT,
                       timezone TEXT,
                       currencyCode TEXT,
                       currencySymbol TEXT,
                       currencySymbol_UTF8 TEXT,
                       currencyConverter REAL)"""
    )
    conn.commit()
    conn.close()


def fetch_geoip_info():
    """
    First get public IP from https://api.ipify.org .
    Then get geoip data from http://www.geoplugin.net/json.gp?ip= .
    """
    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5)
        public_ip.raise_for_status()
        response = requests.get(
            "http://www.geoplugin.net/json.gp?ip={ public_ip.content.decode('utf8') }",
            timeout=5,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"An error occurred while fetching the geoip info: {err}.")
        return None


def store_geoip_info(geoip_info):
    """
    Connect to DB and INSERT all data from geoip.
    """
    conn = sqlite3.connect("db/geoip.db")
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute(
        """INSERT INTO geoip_info (
                        timestamp, ip, status, delay, credit,
                        city, region, regionCode, regionName, areaCode,
                        dmaCode, countryCode, countryName,  inEU, euVATrate,
                        continentCode, continentName, latitude, longitude,
                        locationAccuracyRadius, timezone, currencyCode, currencySymbol,
                        currencySymbol_UTF8, currencyConverter
                        ) VALUES (
                            ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?,
                            ?, ?, ?, ?,
                            ?, ?, ?, ?,
                            ?, ?
                        )""",
        (
            timestamp,
            geoip_info["geoplugin_request"],
            geoip_info["geoplugin_status"],
            geoip_info["geoplugin_delay"],
            geoip_info["geoplugin_credit"],
            geoip_info["geoplugin_city"],
            geoip_info["geoplugin_region"],
            geoip_info["geoplugin_regionCode"],
            geoip_info["geoplugin_regionName"],
            geoip_info["geoplugin_areaCode"],
            geoip_info["geoplugin_dmaCode"],
            geoip_info["geoplugin_countryCode"],
            geoip_info["geoplugin_countryName"],
            geoip_info["geoplugin_inEU"],
            geoip_info["geoplugin_euVATrate"],
            geoip_info["geoplugin_continentCode"],
            geoip_info["geoplugin_continentName"],
            geoip_info["geoplugin_latitude"],
            geoip_info["geoplugin_longitude"],
            geoip_info["geoplugin_locationAccuracyRadius"],
            geoip_info["geoplugin_timezone"],
            geoip_info["geoplugin_currencyCode"],
            geoip_info["geoplugin_currencySymbol"],
            geoip_info["geoplugin_currencySymbol_UTF8"],
            geoip_info["geoplugin_currencyConverter"],
        ),
    )
    conn.commit()
    print(f"Entered geoip data into DB with timestamp {timestamp}.")
    conn.close()


def main():
    """
    Create table if needed.
    Query geoip DB every 60 sec for new data.
    """
    create_table()
    while True:
        geoip_info = fetch_geoip_info()
        if geoip_info:
            store_geoip_info(geoip_info)
        time.sleep(60)


if __name__ == "__main__":
    main()
