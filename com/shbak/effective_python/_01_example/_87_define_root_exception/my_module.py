class Error(Exception):
    pass


class InvalidDensityError(Error):
    pass


class InvalidVolumeError(Error):
    pass


class NagativeDensityError(InvalidDensityError):
    pass

def determine_weight(volume, density):
    if density < 0:
        raise NagativeDensityError('Density must be positive')
    if volume < 0:
        raise InvalidVolumeError('Volume must be positive')
    if volume == 0:
        density / volume
