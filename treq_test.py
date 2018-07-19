from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks
import time

import treq
import config as conf

test_params = conf.test_params


def download_file(reactor, url, destination_filename):
    try:
        print("downloading file")
        destination = open(destination_filename, 'wb')
        d = treq.get(url)
        d.addCallback(treq.collect, destination.write)
        d.addBoth(lambda _: destination.close())
        return d
    except Exception as e:
        print("on download",e)
        return "error downloading the file"


@inlineCallbacks
def test_get_many(reactor, app_url, req_times):
    try:
        params = test_params * req_times
        init_time = temp_time = time.time()
        print("Initializing get testing row")
        for param in params:
            resp = yield treq.get(app_url,
                                  params=param)
            content = yield resp.text()
            print(content, "that took: "+ str(time.time() - temp_time) + " seconds")
            temp_time = time.time()

        print("total time: ", str(time.time() - init_time) + " seconds", req_times,"requests")
        return "end correctly"
    except Exception as e:
        print("on requests", e)
        return "error on requests"

@inlineCallbacks
def test_post_many(reactor, app_url, req_times):
    try:
        params = test_params * req_times
        init_time = temp_time = time.time()
        print("Initializing post testing row")
        for param in params:
            resp = yield treq.post(app_url,
                                  params=param)
            content = yield resp.text()
            print(content, "that took: "+ str(time.time() - temp_time) + " seconds")
            temp_time = time.time()

        print("total time: ", str(time.time() - init_time) + " seconds", req_times,"requests")
        return "end correctly"
    except Exception as e:
        print("on requests", e)
        return "error on requests"

