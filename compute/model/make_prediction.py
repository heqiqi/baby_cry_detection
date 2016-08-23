# -*- coding: utf-8 -*-

import re


__all__ = [
    'BabyCryPredictor'
]


class BabyCryPredictor:
    """
    Class to classify a new audio signal and determine if it's a baby cry
    """

    def __init__(self, model):
        self.model = model

    def classify(self, new_signal):
        """
        Make prediction with trained model

        :param new_signal: 1d array, 34 features
        :return: 1 (it's baby cry); 0 (it's not a baby cry)
        """

        category = self.model.predict(new_signal)

        return self._is_baby_cry(category)

    @staticmethod
    def _is_baby_cry(string):
        """
        String analysis to detect if it is the baby cry category
        :param string: output of model prediction as string
        :return: 1 (it's baby cry); 0 (it's not a baby cry)
        """

        match = re.search('([Bb][Aa][Bb][Yy])[^a-zA-Z]*([Cc][Rr][Yy])*', string)

        if match:
            return 1
        else:
            return 0
