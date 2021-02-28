import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    endpoints = [point for event in A for point in (
        Endpoint(event.start, True), Endpoint(event.finish, False))]

    endpoints.sort(key=lambda e: (e.time, not e.is_start))

    max_sim_events, curr_sim_events = 0, 0
    for endpoint in endpoints:
        if endpoint.is_start:
            curr_sim_events += 1
            max_sim_events = max(max_sim_events, curr_sim_events)
        else:
            curr_sim_events -= 1

    return max_sim_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
