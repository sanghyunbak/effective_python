import logging

from com.shbak.effective_python._01_example._87_define_root_exception import my_module

if __name__ == '__main__':
    try:
        weight = my_module.determine_weight(1, -1)
    except my_module.NagativeDensityError as exc:
        raise ValueError('Density must be positive') from exc
    except my_module.InvalidDensityError:
        weight = 0
    except my_module.Error:
        logging.exception('Unexpected Error')
    except Exception:
        logging.exception('Bug in the API Code')
