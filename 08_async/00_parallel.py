import numpy as np
import logging
N = 1000

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

logger.info('Losowanie macierzy...')
A = np.random.randint(0, N**2, size=(N, N)).astype(float)
logger.info('Odwracanie macierzy...')
A_inv = np.linalg.inv(A)
logger.info('Koniec obliczeń...')
