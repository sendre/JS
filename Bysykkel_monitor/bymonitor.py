import json
import urllib.request
import pandas as pd

def fetch_json_as_dict(url, identifier):
    """Fetches the json object from the url, and returns a dictionary
    representation of the json object.

    url - url to request json
    identifier - string describing our application"""

    try:
        req = urllib.request.Request(url)
        req.add_header('Client-Identifier', identifier)
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        exit(1)
    except urllib.error.HTTPError as e:
        print(e)
        exit(1)
    else:
        dict_json = json.loads(response.read())
        return dict_json

def list_stations(my_id, auto_discovery_url):
    """Prints the different stations and the number of available bikes and locks

    my_id - string describing our application
    auto_discovery_url - auto discovery url"""

    auto_discovery_dict = fetch_json_as_dict(auto_discovery_url, my_id)

    aut_data = auto_discovery_dict['data']
    aut_language = list(aut_data.keys())[0] #index zero for simplicity in this task
    aut_feeds = aut_data[aut_language]['feeds']

    station_info_df = {}
    station_status_df = {}
    for tmp_dict in aut_feeds:
        if tmp_dict['name'] == 'station_information':
            station_info_dict = fetch_json_as_dict(tmp_dict['url'], my_id)
            station_info_df = pd.DataFrame(station_info_dict['data']['stations'])

        if tmp_dict['name'] == 'station_status':
            station_status_dict = fetch_json_as_dict(tmp_dict['url'], my_id)
            station_status_df = pd.DataFrame(station_status_dict['data']['stations'])

    #inner join between the two tables
    merged_df = pd.merge(station_info_df, station_status_df, on=['station_id'],
                                                             how='inner')

    merged_df.rename(columns={"num_bikes_available": "Ledige sykler",
                              "num_docks_available": "Ledige låser",
                              "name": "Stasjon"}, inplace=True)

    print(merged_df[['Stasjon', 'Ledige sykler', 'Ledige låser']].to_string(index=False))


if __name__=='__main__':
    my_id = 'sindre_kodeoppgave-bymonitor'
    auto_discovery_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/gbfs.json'
    list_stations(my_id, auto_discovery_url)
