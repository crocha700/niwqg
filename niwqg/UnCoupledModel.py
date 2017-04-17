import numpy as np
from . import Kernel

class Model(Kernel.Kernel):
    """ A subclass that represents the YBJ-QG uncoupled model """

    def __init__(
        self,
        **kwargs
        ):

        super(Model, self).__init__(**kwargs)

    def _allocate_variables(self):
        """ Allocate variables in memory """

        self.dtype_real = np.dtype('float64')
        self.dtype_cplx = np.dtype('complex128')
        self.shape_real = (self.ny, self.nx)
        self.shape_cplx = (self.ny, self.nx)

        # vorticity
        self.q  = np.zeros(self.shape_real,  self.dtype_real)
        self.qh = np.zeros(self.shape_cplx,  self.dtype_cplx)
        self.qh0 = np.zeros(self.shape_cplx, self.dtype_cplx)
        self.qh1 = np.zeros(self.shape_cplx, self.dtype_cplx)

        # stream function
        self.p  = np.zeros(self.shape_real,  self.dtype_real)
        self.ph = np.zeros(self.shape_cplx,  self.dtype_cplx)

        # wave amplitude
        self.phi = np.zeros(self.shape_real,  self.dtype_cplx)
        self.phih = np.zeros(self.shape_cplx,  self.dtype_cplx)

    def _calc_grad_phi(self):
        """ Calculates grad phi """
        self.phix, self.phiy = self.ifft(self.ik*self.phih), self.ifft(self.il*self.phih)

    def _invert(self):
        """ From qh compute ph and compute velocity. """
        self.ph = -self.wv2i*self.qh

    def _initialize_class_diagnostics(self):
        pass

    def _calc_class_derived_fields(self):
        pass
