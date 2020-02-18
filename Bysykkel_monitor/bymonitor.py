import json
import urllib.request
import pandas as pd

def write_df_to_json_file(df, filename):
    """Writes the dataframe to a file in json format

    df - pandas dataframe containing the station information returned by the
    list_stations function
    filename - name of json file"""
    df = df[['Stasjon', 'Ledige sykler', 'Ledige låser']]
    df.to_json(filename, orient="records")


def fetch_json_as_dict(url, identifier):
    """Fetches the json object from the url, and returns a dictionary
    representation of the json object. If an error occurs, the error message is
    printed and None is returned

    url - url to request json
    identifier - string describing our application"""

    try:
        req = urllib.request.Request(url)
        req.add_header('Client-Identifier', identifier)
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        return None, e.status
    except urllib.error.HTTPError as e:
        return None, e.status
    else:
        dict_json = json.loads(response.read())
        return dict_json, 200

def list_stations(my_id, auto_discovery_url, print_stations=True):
    """Prints the different stations and the number of available bikes and locks.
    If an error occurs, None is returned. Otherwise, the dataframe containing the
    information is returned

    my_id - string describing our application
    auto_discovery_url - auto discovery url
    print_stations - should the stations be printed? default True"""

    auto_discovery_dict, status = fetch_json_as_dict(auto_discovery_url, my_id)
    if auto_discovery_dict is None:
        return None, status

    aut_data = auto_discovery_dict['data']
    aut_language = list(aut_data.keys())[0] #index zero for simplicity in this task
    aut_feeds = aut_data[aut_language]['feeds']

    station_info_df = {}
    station_status_df = {}
    for tmp_dict in aut_feeds:
        if tmp_dict['name'] == 'station_information':
            station_info_dict, status = fetch_json_as_dict(tmp_dict['url'], my_id)
            if station_info_dict is None:
                return None, status
            station_info_df = pd.DataFrame(station_info_dict['data']['stations'])

        if tmp_dict['name'] == 'station_status':
            station_status_dict, status = fetch_json_as_dict(tmp_dict['url'], my_id)
            if station_status_dict is None:
                return None, status
            station_status_df = pd.DataFrame(station_status_dict['data']['stations'])

    #inner join between the two tables
    merged_df = pd.merge(station_info_df, station_status_df, on=['station_id'],
                                                             how='inner')

    merged_df.rename(columns={"num_bikes_available": "Ledige sykler",
                              "num_docks_available": "Ledige låser",
                              "name": "Stasjon"}, inplace=True)
    if print_stations:
        print(merged_df[['Stasjon', 'Ledige sykler', 'Ledige låser']].to_string(index=False))
    return merged_df, 200


if __name__=='__main__':
    my_id = 'sindre_kodeoppgave-bymonitor'
    auto_discovery_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/gbfs.json'
    ret, status = list_stations(my_id, auto_discovery_url)
    if ret is None:
        exit(1)

    #writes the data returned by list_stations() to a json file: stations_data.json
    write_df_to_json_file(ret, 'stations_data.json')
