import flask
import urllib2
import urllib3
import yaml

APP = flask.Flask(__name__)


@APP.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person:
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    # Import the requested version (2 or 3) of urllib
    if urllib_version == 2:
        http = urllib2.PoolManager()
    elif urllib_version == 3:
        http = urllib3.PoolManager()
    else:
        raise ValueError("Invalid urllib version!")

    # Fetch and print the requested URL
    r = http.request("GET", url)

    print(r.data)


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(
        stream, Loader=yaml.Loader
    )  # deserializing data
    return deserialized_data


def authenticate(password):
    # Assert that the password is correct
    if password != "Iloveyou":
        raise ValueError("Invalid password!")

    print("Successfully authenticated!")


if __name__ == "__main__":
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    CHOICE = input("Select vulnerability: ")
    if CHOICE == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif CHOICE == "2":
        URLIB_VERSION = input("Choose version of urllib: ")
        fetch_website(URLIB_VERSION, url="https://www.google.com")
    elif CHOICE == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif CHOICE == "4":
        PASSWORD = input("Enter master password: ")
        authenticate(PASSWORD)
