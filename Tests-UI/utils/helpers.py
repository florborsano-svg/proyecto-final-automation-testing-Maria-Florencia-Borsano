import logging
import pathlib

# 1) Carpeta donde se almacenarán los logs:

audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

# 2) Configuracion global
logging.basicConfig(
    filename = audit_dir / 'suit.log',
    level = logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt = '%d/%m/%Y %H:%M:%S',
    force=True
)
# 3) Logger especifico que usarán los tests
logger = logging.getLogger('talentolab')