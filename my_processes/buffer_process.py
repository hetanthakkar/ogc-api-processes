import logging
from shapely.geometry import shape, mapping
from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

LOGGER = logging.getLogger(__name__)

PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'buffer',
    'title': {'en': 'Buffer Process'},
    'description': {'en': 'Draws a shape around a point at a given distance.'},
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'inputs': {
        'geom': {
            'title': 'Input Geometry',
            'description': 'A GeoJSON point',
            'schema': {'type': 'object'},
            'minOccurs': 1,
            'maxOccurs': 1
        },
        'distance': {
            'title': 'Buffer Distance',
            'description': 'Distance in degrees',
            'schema': {'type': 'number'},
            'minOccurs': 1,
            'maxOccurs': 1
        }
    },
    'outputs': {
        'result': {
            'title': 'Buffered Geometry',
            'schema': {'type': 'object'}
        }
    }
}


class BufferProcessor(BaseProcessor):
    def __init__(self, processor_def):
        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data, outputs=None):
        geom_input = data.get('geom')
        distance = data.get('distance')

        if geom_input is None:
            raise ProcessorExecuteError('Missing input: geom')
        if distance is None:
            raise ProcessorExecuteError('Missing input: distance')

        geom = shape(geom_input)
        buffered = geom.buffer(float(distance))

        return 'application/json', {'id': 'result', 'value': mapping(buffered)}