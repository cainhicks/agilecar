import logging

logger = logging.getLogger(__name__)

def map(from_obj, to_obj):
    for index, name in enumerate(from_obj.cleaned_data):
        try:
            setattr(to_obj, name, from_obj.cleaned_data[name])
        except TypeError as ex:
            logger.error("Exception with name {0} value {1} message {2}".format(name, index, ex.message))