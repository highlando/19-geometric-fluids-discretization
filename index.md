---
layout: index
---

Seminar - Geometric formulations of inviscid fluids and their discretization - OvGU - 2019
-----


| Day | Time | Place |
| ------- | ------ | ------- |
| Wednesday | 11:00-13:00 | tba |

Consultation hours: Please make an appointment by email.



### Topics and Literature

#### Variational formulation of ideal fluid

Develop variational formulation of ideal fluid, possibly including from the general perspective of Euler-Poincare reduction
  
:memo: V. I. Arnold, *Mathematical Methods of Classical Mechanics*, Second. ed. Springer, 1989 (Appendix A).

:memo: J. E. Marsden and T. S. Ratiu, *Introduction to Mechanics and Symmetry: A Basic Exposition of Classical Mechanical Systems*, Third ed. New York: Springer-Verlag, 1999.


#### Hamiltonian formulation of ideal fluid

Develop Hamiltonian formulation of ideal fluid dynamics, including conserved quantities in 2D and 3D

:memo: J. E. Marsden and A. Weinstein, *Coadjoint orbits, vortices, and Clebsch variables for incompressible fluids,* Phys. D Nonlinear Phenom., vol. 7, no. 1–3, pp. 305–323, May 1983.

:memo: V. I. Arnold and B. A. Khesin, Topological Methods in Hydrodynamics. New York: Springer, 1998.


#### Algebraic, structure preserving numerical method for ideal fluid dynamics

Math: Develop the discretization of the 2D ideal fluid proposed by Zeitlin based on the work by Hoppe

CS: Develop an implementation of the algorithm proposed by Zeitlin

:memo: V. Y. Zeitlin, *Finite-mode analogs of 2D ideal hydrodynamics: Coadjoint orbits and local canonical structure,* Phys. D Nonlinear Phenom., vol. 49, no. 3, pp. 353–362, Apr. 1991.

:memo: J. Hoppe, *Diffeomorphism Groups, Quantization, and SU(∞),* Int. J. Mod. Phys. A, vol. 04, no. 19, pp. 5235–5248, Nov. 1989.

:memo: S. J. Rankin, *SU(∞) and the large-N limit,* Ann. Phys. (N. Y)., vol. 218, no. 1, pp. 14–50, Aug. 1992.

:memo: R. I. McLachlan, *Explicit Lie-Poisson integration and the Euler equations,* Phys. Rev. Lett., vol. 71, no. 19, pp. 3043–3046, Nov. 1993.


#### Madelung transform

Develop the Madelung transform as a hydrodynamical model for quantum mechanics, with an emphasis on the geometric perspective as a momentum map

Optional: connection to [Chern et al. 2016]

:memo: D. Fusca, *The Madelung transform as a momentum map,* J. Geom. Mech., vol. 9, no. 2, pp. 157–165, 2017.,

:memo: E. Madelung, *Quantentheorie in hydrodynamischer Form,* Zeitschrift für Phys., vol. 40, no. 3–4, pp. 322–326, Mar. 1927.

:memo: E. Madelung, *Eine anschauliche Deutung der Gleichung von Schrödinger,* Naturwissenschaften, vol. 14, no. 45, pp. 1004–1004, Nov. 1926.

:memo: A. Chern, F. Knöppel, U. Pinkall, P. Schröder, and S. Weißmann, *Schrödinger’s smoke,* ACM Trans. Graph., vol. 35, no. 4, pp. 1–13, Jul. 2016.

:memo: M. Schönberg, *On the hydrodynamical model of the quantum mechanics,* Nuovo Cim., vol. 12, no. 1, pp. 103–133, Jul. 1954.


#### Spectral, structure preserving integrator for ideal fluid dynamics

Develop an implementation of the algorithm proposed by Liu et al. 2015

:memo: J. E. Marsden and A. Weinstein, *Coadjoint orbits, vortices, and Clebsch variables for incompressible fluids,* Phys. D Nonlinear Phenom., vol. 7, no. 1–3, pp. 305–323, May 1983.

:memo: T. de Witt, C. Lessig, and E. Fiume, *Fluid Simulation Using Laplacian Eigenfunctions,* ACM Trans. Graph., vol. 31, no. 1, pp. 1–11, Jan. 2012.


#### Variational, structure preserving numerical integrator for arbitrary meshes

Math: Develop the variational structure preserving integrator proposed by Pavlov et al., possibly including the extensions in Gawlik
CS: Implement the algorithm presented by Mullen et al. (2D, on a regular grid or using PyDec)

:memo: E. S. Gawlik, P. Mullen, D. Pavlov, J. E. Marsden, and M. Desbrun, *Geometric, variational discretization of continuum theories,* Phys. D Nonlinear Phenom., vol. 240, no. 21, pp. 1724–1760, Oct. 2011.

:memo: D. Pavlov, P. Mullen, Y. Tong, E. Kanso, J. E. Marsden, and M. Desbrun, *Structure-preserving discretization of incompressible fluids,* Phys. D Nonlinear Phenom., vol. 240, no. 6, pp. 443–458, Mar. 2011.

:memo: P. Mullen, K. Crane, D. Pavlov, Y. Tong, and M. Desbrun, *Energy-Preserving Integrators for Fluid Animation,* ACM Trans. Graph. (Proceedings SIGGRAPH 2009), vol. 28, no. 3, pp. 1--8, 2009.


#### Vorticity-based, structure preserving discretization of fluids

Develop an implementation of the technique proposed by Elcott et al.

:memo: S. Elcott, Y. Tong, E. Kanso, P. Schröder, and M. Desbrun, *Stable, Circulation-Preserving, Simplicial Fluids,* ACM Trans. Graph., vol. 26, no. 1, 2007.
