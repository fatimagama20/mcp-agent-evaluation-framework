import time


def test_response_latency():

    start = time.time()

    time.sleep(1)

    end = time.time()

    latency = end - start

    assert latency < 2