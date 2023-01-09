#!/usr/bin/env python3
from flts import vuelo_nonstop, vuelo_1stop, vuelo_con_escala, vuelo_3stop, vuelo_tbs, vuelo_longest
import unittest
from app import sell_this_flight

class Test_to_overcome_humanity(unittest.TestCase):

    without_stops = sell_this_flight(vuelo_nonstop)
    with_3_connections = sell_this_flight(vuelo_3stop)
    with_1_connection  = sell_this_flight(vuelo_1stop)
    with_longest_so_far = sell_this_flight(vuelo_longest)
    with_escala = sell_this_flight(vuelo_con_escala)


    def test_flights(self):
        self.assertEqual(self.with_3_connections.ordered_flights(), ['AS 453', 'DE 2033', 'LH 1242'])
        self.assertEqual(self.without_stops.ordered_flights(), ['UA 1441'])
        self.assertEqual(self.with_1_connection.ordered_flights(), ['AM 479', 'AM 628'])
        self.assertEqual(self.with_longest_so_far.ordered_flights(), ['OS 7791', 'AA 536', 'AA 35'])

    def test_cos(self):
        self.assertEqual(self.with_3_connections.ordered_cos(), ['Y', 'Y', 'Y'])
        self.assertEqual(self.without_stops.ordered_cos(), ['K'])
        self.assertEqual(self.with_1_connection.ordered_cos(), ['V', 'V'])
        self.assertEqual(self.with_longest_so_far.ordered_cos(), ['Y', 'Y', 'W'])


    def test_date(self):
        # self.assertEqual(self.with_3_connections.ordered_dates(), ['12Jan', '12Jan', '13Jan'])
        self.assertEqual(self.without_stops.ordered_dates(), ['26Jan'])
        self.assertEqual(self.with_1_connection.ordered_dates(), ['12Jan', '13Jan'])
        self.assertEqual(self.with_longest_so_far.ordered_dates(), ['04Jan', '05Jan', '05Jan'])
        self.assertEqual(self.with_escala.ordered_dates(), ['12Jan', '12Jan'])

    def test_cities(self):
        self.assertEqual(self.with_3_connections.ordered_citypairs(), ['IAHSEA', 'SEAFRA', 'FRAVIE'])
        self.assertEqual(self.without_stops.ordered_citypairs(), ['IAHSAL'])
        self.assertEqual(self.with_1_connection.ordered_citypairs(), ['IAHMEX', 'MEXSAL'])
        self.assertEqual(self.with_longest_so_far.ordered_citypairs(), ['LHREWR', 'EWRDFW', 'DFWAKL'])



if __name__ == "__main__":
    unittest.main()

# ['Aeromexico 479', 'Aeromexico 628']
# ['V', 'V']
# ['12Jan', '12Jan ']
# ['IAHMEX', 'MEXSAL']



# ['United 1441']
# ['K']
# ['26Jan']
# ['IAHSAL']

# ['Alaska Airlines 453', 'Condor 2033', 'Lufthansa 1242']
# ['Y', 'Y', 'Y']
# ['12Jan', '12Jan ', '13Jan ']
# ['IAHSEA', 'SEAFRA', 'FRAVIE']
