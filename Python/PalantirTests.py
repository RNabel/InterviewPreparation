import collections
import unittest

import sys
from StringIO import StringIO

import Palantir


class Tests(unittest.TestCase):
    def setUp(self):
        Palantir.inside_traders = collections.defaultdict(set)
        Palantir.stock_values = {}
        Palantir.trades = []

    def testStringParsing(self):
        st = "11|Bob|BUY|100000"
        Palantir.stock_values[11] = 2
        res = Palantir.get_details(st)
        self.assertEquals(11, res[0])
        self.assertEquals("Bob", res[1])
        self.assertEquals(-200000, res[2])

    def testProcessTrade(self):
        st = "1|Bob|BUY|2"
        Palantir.stock_values[1] = 10
        Palantir.process_new_line(st)

        self.assertEquals(-20, Palantir.trader_profits["Bob"])

    def testProcessTradeTwoDays(self):
        st = "1|Bob|BUY|2"
        st2 = "2|Bob|BUY|3"
        Palantir.stock_values[1] = 10
        Palantir.stock_values[2] = 40

        Palantir.process_new_line(st)
        Palantir.process_new_line(st2)

        self.assertEquals(-140, Palantir.trader_profits["Bob"])
        self.assertEquals(2, len(Palantir.trades))

    def testProcessBuyAndSell(self):
        st = "1|Bob|BUY|2"
        st2 = "2|Bob|SELL|2"
        Palantir.stock_values[1] = 10
        Palantir.stock_values[2] = 40

        Palantir.process_new_line(st)
        Palantir.process_new_line(st2)

        self.assertEquals(60, Palantir.trader_profits["Bob"])
        self.assertEquals(2, len(Palantir.trades))

    def testProcessMultipleTraders(self):
        Palantir.stock_values[1] = 10
        Palantir.stock_values[2] = 40
        first = "1|Bob|BUY|2"
        second = "2|Bob|SELL|2"
        Palantir.process_new_line(first)
        Palantir.process_new_line(second)

        first = "1|Mary|BUY|5"
        second = "2|Mary|SELL|3"
        Palantir.process_new_line(first)
        Palantir.process_new_line(second)

        self.assertEquals(60, Palantir.trader_profits["Bob"])
        self.assertEquals(70, Palantir.trader_profits["Mary"])

    def testUndoTrades(self):
        Palantir.stock_values[1] = 3
        Palantir.stock_values[2] = 4
        Palantir.stock_values[3] = 5
        Palantir.stock_values[4] = 6
        first = "1|Bob|BUY|1"
        second = "2|Bob|BUY|1"
        third = "3|Bob|BUY|1"
        fourth = "4|Bob|SELL|3"
        Palantir.process_new_line(first)
        Palantir.process_new_line(second)
        Palantir.process_new_line(third)
        self.assertEquals(-12, Palantir.trader_profits["Bob"])
        Palantir.process_new_line(fourth)
        self.assertEquals(9, Palantir.trader_profits["Bob"])

    def testInsideTrader(self):
        Palantir.stock_values[1] = 1
        Palantir.stock_values[2] = 1000001
        first = "1|Bob|BUY|5"
        second = "2|Bob|SELL|5"

        Palantir.process_new_line(first)
        Palantir.process_new_line(second)

        self.assertEquals(5000000, Palantir.trader_profits["Bob"])

    def testOutputSingle(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            Palantir.stock_values[1] = 1
            Palantir.stock_values[2] = 1000001
            first = "1|Bob|BUY|5"
            second = "2|Bob|SELL|5"

            Palantir.process_new_line(first)
            Palantir.process_new_line(second)
            Palantir.output_results()

            output = out.getvalue().strip()
            self.assertEquals("2 Bob", output)
        finally:
            sys.stdout = saved_stdout

    def testOutputMultidayAndTrader(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            Palantir.stock_values[1] = 1
            Palantir.stock_values[2] = 1000001
            Palantir.stock_values[5] = 1
            Palantir.stock_values[6] = 1000001
            first = "1|Bob|BUY|5"
            second = "2|Bob|SELL|5"
            Palantir.process_new_line(first)
            Palantir.process_new_line(second)
            first = "1|Mary|BUY|5"
            second = "2|Mary|SELL|5"
            Palantir.process_new_line(first)
            Palantir.process_new_line(second)
            first = "5|Mary|BUY|5"
            second = "6|Mary|SELL|5"
            Palantir.process_new_line(first)
            Palantir.process_new_line(second)
            first = "5|Oct|BUY|5"
            second = "6|Oct|SELL|5"
            Palantir.process_new_line(first)
            Palantir.process_new_line(second)

            Palantir.output_results()

            output = out.getvalue().strip()
            self.assertEquals("2 Bob\n2 Mary\n6 Mary\n6 Oct", output)
        finally:
            sys.stdout = saved_stdout

    def testSampleInput(self):
        datafeed = [
            "16",
            "0|20",
            "0|Kristi|SELL|3000",
            "0|Will|BUY|5000",
            "0|Tom|BUY|50000",
            "0|Shilpa|BUY|1500",
            "1|Tom|BUY|1500000",
            "3|25",
            "5|Shilpa|SELL|1500000",
            "8|Kristi|SELL|600000",
            "9|Shilpa|BUY|500",
            "10|15",
            "11|5",
            "14|Will|BUY|100000",
            "15|Will|BUY|100000",
            "16|Will|BUY|100000",
            "17|25"
        ]

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            Palantir.findPotentialInsiderTraders(datafeed)
            output = out.getvalue().strip()
            self.assertEquals("1|Tom\n8|Kristi", output)

        finally:
            sys.stdout = saved_stdout

    def testSampleInput3(self):
        datafeed = [
            "20",
            "0|1000",
            "0|Shilpa|BUY|30000",
            "0|Will|BUY|50000",
            "0|Tom|BUY|40000",
            "0|Kristi|BUY|15000",
            "1|Kristi|BUY|11000",
            "1|Tom|BUY|1000",
            "1|Will|BUY|19000",
            "1|Shilpa|BUY|25000",
            "2|1500",
            "2|Will|SELL|7000",
            "2|Shilpa|SELL|8000",
            "2|Kristi|SELL|6000",
            "2|Tom|SELL|9000",
            "3|500",
            "38|1000",
            "78|Shilpa|BUY|30000",
            "79|Kristi|BUY|60000",
            "80|1100",
            "81|1200",
        ]

        it = Palantir.findPotentialInsiderTraders(datafeed)

        out = ["0|Kristi",
               "0|Shilpa",
               "0|Tom",
               "0|Will",
               "1|Kristi",
               "1|Shilpa",
               "1|Will",
               "2|Kristi",
               "2|Shilpa",
               "2|Tom",
               "2|Will",
               "78|Shilpa",
               "79|Kristi"]

        for i, j in zip(it, out):
            self.assertEquals(i, j)

    def testSampleInputEmpty(self):
        datafeed = [
            "0",
            "0|10"
        ]

        it = Palantir.findPotentialInsiderTraders(datafeed)

        out = []

        for i, j in zip(it, out):
            self.assertEquals(i, j)


    def testSampleInputBoundary(self):
        datafeed = [
            "3",
            "0|1001000",
            "0|Shilpa|SELL|5",
            "1|Shilpa|SELL|9",
            "1|Shilpa|SELL|9",
            "2|1",
        ]

        it = Palantir.findPotentialInsiderTraders(datafeed)

        out = [
            "0|Shilpa",
            "1|Shilpa",
               ]
        it_out = list(it)
        for i, j in zip(out, it_out):
            self.assertEquals(i, j)
        self.assertEquals(len(out), len(it_out))
