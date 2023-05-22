import json

import yaml
from posttroll.message import datetime_encoder
from posttroll.subscriber import create_subscriber_from_dict_config
from pyresample.area_config import load_area
from contextlib import closing
from trollsift.parser import Parser
import argparse

def write_message_to_file(msg, filename, area_file):
    with open(filename, "w") as fd:
        json.dump([message_to_json(area_file, msg.data)],
                  fd, default=datetime_encoder)


def message_to_json(area_file, info):
    area = load_area(area_file, info["area"])
    return dict_from_info(info, area)


def append_message_to_file(msg, filename, area_file):
    try:
        with open(filename) as fd:
            data = json.load(fd)
    except FileNotFoundError:
        data = []
    data.append(message_to_json(area_file, msg.data))
    with open(filename, "w") as fd:
        json.dump(data, fd, default=datetime_encoder)

def subscribe_and_write(filename, area_file, subscriber_settings):
    with closing(create_subscriber_from_dict_config(subscriber_settings)) as sub:
        for message in sub.recv():
            append_message_to_file(message, filename, area_file)


def read_config(yaml_file):
    with open(yaml_file) as fd:
        data = yaml.safe_load(fd.read())
    return data


def main(args=None):
    """Main script."""
    parsed_args = parse_args(args=args)
    config = read_config(parsed_args.config_file)
    subscribe_and_write(config["filename"],
                        config["area_file"],
                        config["subscriber_settings"])

def parse_args(args=None):
    """Parse commandline arguments."""
    parser = argparse.ArgumentParser("Message writer",
                                     description="Write message into a json file for wms")
    parser.add_argument("config_file",
                        help="The configuration file to run on.")
    parser.add_argument('files', nargs='*', action='store')
    return parser.parse_args(args)

def create_list_from_files(filename, area_file, filepattern, list_of_files):
    parser = Parser(filepattern)
    data = []
    for f in list_of_files:
        info = parser.parse(f)
        info["uri"] = f
        area = load_area(area_file, info["area"])
        data.append(dict_from_info(info, area))
    with open(filename, "w") as fd:
        json.dump(data, fd, default=datetime_encoder)


def dict_from_info(info, area):
    return {"uri": info["uri"],
            "layer": info["product"],
            "start_time": info["start_time"],
            "area_extent": area.area_extent,
            "proj4": area.proj_str
            }


def files_to_list(args=None):
    """Main script."""
    parsed_args = parse_args(args=args)
    config = read_config(parsed_args.config_file)

    create_list_from_files(config["filename"], config["area_file"], config["filepattern"], parsed_args.files)
