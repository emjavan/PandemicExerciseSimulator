#!/usr/bin/env python3
import logging
import sys

logger = logging.getLogger(__name__)


class Day:

    def __init__(self, num:int):
        try:
            assert self._validate_input(num) == True
        except AssertionError as e:
            raise Exception('Day class must be initialized with positive integer') from e
            sys.exit(1)
        self.number_of_days = int(num)
        logger.info(f'instantiated Day object with seed {num}')
        logger.debug(f'{self}')
        return

    def __str__(self) -> str:
        return(f'Day:{self.number_of_days}')

    def _validate_input(self, num:int) -> bool:
        return(str(num).isnumeric())

    def increment_day(self, num:int):
        try:
            assert self._validate_input(num) == True
        except AssertionError as e:
            raise Exception('Day class can only be incremented by a positive integer') from e
            sys.exit(1)
        self.number_of_days += int(num)
        return


