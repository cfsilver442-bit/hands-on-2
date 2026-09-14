import sys, unittest

from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from asap3 import EMT

from md import calcenergy


class MdTests(unittest.TestCase):
    def test_calcenergy(self):

        atoms = FaceCenteredCubic(
            directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            symbol="Cu",
            size=(3, 3, 3),
            pbc=True,
        )

        atoms.calc = EMT()
        MaxwellBoltzmannDistribution(atoms, temperature_K=300)

        epot, ekin, temp, etot = calcenergy(atoms)

        self.assertAlmostEqual(etot, epot + ekin)
        self.assertGreater(ekin, 0)
        self.assertGreater(temp, 0)


if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
