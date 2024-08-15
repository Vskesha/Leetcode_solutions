import unittest
from itertools import pairwise
from math import comb
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        digits = nums[0]
        for prev, curr in pairwise(nums):
            if curr < prev:
                digits += curr - prev
                if digits < 0:
                    return 0

        return comb(digits + len(nums), digits) % mod


class Solution1:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums) - 1

        digits = nums[0] + 1
        for prev, curr in pairwise(nums):
            if curr < prev:
                digits += curr - prev
                if digits <= 0:
                    return 0

        ans = nd = 1
        for i in range(1, digits):
            nd = nd * (n + i) // i
            ans = (ans + nd) % mod
        return ans


class Solution2:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums) - 1

        digits = nums[0] + 1
        for prev, curr in pairwise(nums):
            if curr < prev:
                digits += curr - prev
                if digits <= 0:
                    return 0

        return sum(comb(k + n, k) % mod for k in range(digits)) % mod


class Solution3:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        digits = nums[0] + 1
        for prev, curr in pairwise(nums):
            if curr < prev:
                digits += curr - prev
                if digits <= 0:
                    return 0

        dp = [1] * digits
        for _ in range(len(nums) - 1):
            for i in range(1, digits):
                dp[i] = (dp[i] + dp[i - 1]) % mod

        return sum(dp) % mod


# Time Limit Exceeded
class Solution4:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        dp = [1] * (nums[0] + 1)
        z = 0

        for i in range(1, n):
            ndp = [0] * (nums[i] + 1)
            diff = max(0, nums[i] - nums[i - 1])
            for inc in range(diff + z, nums[i] + 1):
                ndp[inc] = sum(dp[z : (inc - diff + 1)]) % mod
            z += diff
            dp = ndp

        return sum(dp) % mod


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countOfPairs"] * 3,
            "kwargs": [
                dict(nums=[2, 3, 2]),
                dict(nums=[5, 5, 5, 5]),
                dict(
                    nums=[
                        20,
                        22,
                        25,
                        25,
                        25,
                        26,
                        26,
                        28,
                        29,
                        31,
                        32,
                        32,
                        34,
                        35,
                        36,
                        38,
                        39,
                        39,
                        39,
                        40,
                        41,
                        42,
                        44,
                        44,
                        44,
                        45,
                        45,
                        46,
                        47,
                        48,
                        48,
                        50,
                        50,
                        50,
                        51,
                        52,
                        53,
                        55,
                        55,
                        56,
                        56,
                        56,
                        57,
                        58,
                        59,
                        59,
                        61,
                        62,
                        63,
                        64,
                        64,
                        64,
                        65,
                        66,
                        67,
                        67,
                        67,
                        67,
                        68,
                        70,
                        71,
                        71,
                        72,
                        72,
                        73,
                        74,
                        78,
                        79,
                        80,
                        82,
                        82,
                        83,
                        83,
                        83,
                        84,
                        88,
                        88,
                        88,
                        89,
                        92,
                        94,
                        97,
                        98,
                        98,
                        100,
                        101,
                        101,
                        108,
                        109,
                        109,
                        111,
                        112,
                        113,
                        114,
                        118,
                        119,
                        120,
                        120,
                        121,
                        124,
                        125,
                        125,
                        126,
                        126,
                        128,
                        130,
                        131,
                        132,
                        133,
                        136,
                        136,
                        137,
                        138,
                        138,
                        139,
                        140,
                        140,
                        140,
                        145,
                        147,
                        147,
                        147,
                        150,
                        151,
                        151,
                        152,
                        155,
                        155,
                        156,
                        157,
                        159,
                        159,
                        160,
                        160,
                        161,
                        161,
                        162,
                        162,
                        166,
                        167,
                        169,
                        170,
                        171,
                        171,
                        174,
                        175,
                        176,
                        178,
                        179,
                        179,
                        182,
                        183,
                        183,
                        183,
                        185,
                        185,
                        186,
                        187,
                        189,
                        190,
                        190,
                        191,
                        192,
                        192,
                        193,
                        195,
                        195,
                        195,
                        196,
                        197,
                        199,
                        199,
                        199,
                        199,
                        200,
                        200,
                        201,
                        201,
                        202,
                        202,
                        203,
                        203,
                        204,
                        207,
                        208,
                        210,
                        210,
                        210,
                        211,
                        212,
                        213,
                        214,
                        217,
                        217,
                        217,
                        218,
                        218,
                        221,
                        222,
                        223,
                        224,
                        225,
                        225,
                        226,
                        228,
                        229,
                        230,
                        230,
                        231,
                        232,
                        233,
                        233,
                        233,
                        239,
                        240,
                        241,
                        242,
                        243,
                        243,
                        243,
                        244,
                        246,
                        246,
                        247,
                        247,
                        248,
                        249,
                        250,
                        250,
                        252,
                        252,
                        252,
                        252,
                        253,
                        253,
                        254,
                        254,
                        257,
                        257,
                        258,
                        259,
                        259,
                        260,
                        261,
                        262,
                        264,
                        264,
                        266,
                        271,
                        272,
                        272,
                        273,
                        275,
                        275,
                        276,
                        278,
                        278,
                        279,
                        280,
                        282,
                        282,
                        283,
                        283,
                        283,
                        283,
                        284,
                        288,
                        289,
                        290,
                        291,
                        291,
                        293,
                        295,
                        296,
                        296,
                        297,
                        300,
                        301,
                        302,
                        302,
                        305,
                        305,
                        308,
                        308,
                        308,
                        309,
                        312,
                        314,
                        316,
                        316,
                        317,
                        317,
                        319,
                        319,
                        319,
                        319,
                        321,
                        321,
                        322,
                        322,
                        323,
                        323,
                        324,
                        324,
                        325,
                        326,
                        327,
                        329,
                        329,
                        330,
                        330,
                        331,
                        331,
                        334,
                        335,
                        336,
                        336,
                        337,
                        338,
                        338,
                        343,
                        344,
                        344,
                        345,
                        346,
                        347,
                        349,
                        350,
                        351,
                        351,
                        354,
                        354,
                        356,
                        356,
                        357,
                        361,
                        362,
                        363,
                        364,
                        365,
                        365,
                        365,
                        367,
                        368,
                        368,
                        369,
                        370,
                        370,
                        370,
                        371,
                        374,
                        375,
                        377,
                        378,
                        379,
                        380,
                        380,
                        381,
                        382,
                        382,
                        383,
                        383,
                        384,
                        385,
                        386,
                        387,
                        388,
                        391,
                        391,
                        392,
                        393,
                        394,
                        394,
                        395,
                        395,
                        396,
                        398,
                        399,
                        401,
                        402,
                        402,
                        405,
                        409,
                        409,
                        411,
                        412,
                        414,
                        414,
                        414,
                        416,
                        416,
                        417,
                        418,
                        418,
                        419,
                        420,
                        421,
                        424,
                        428,
                        428,
                        428,
                        428,
                        429,
                        429,
                        429,
                        430,
                        431,
                        432,
                        433,
                        434,
                        434,
                        435,
                        436,
                        438,
                        440,
                        442,
                        443,
                        444,
                        445,
                        446,
                        446,
                        446,
                        446,
                        451,
                        451,
                        452,
                        453,
                        453,
                        453,
                        454,
                        458,
                        461,
                        462,
                        462,
                        462,
                        462,
                        463,
                        464,
                        466,
                        467,
                        467,
                        468,
                        469,
                        469,
                        470,
                        474,
                        478,
                        478,
                        479,
                        480,
                        481,
                        482,
                        482,
                        482,
                        484,
                        484,
                        489,
                        490,
                        491,
                        493,
                        493,
                        494,
                        495,
                        496,
                        497,
                        498,
                        498,
                        498,
                        500,
                        501,
                        501,
                        502,
                        505,
                        506,
                        506,
                        507,
                        508,
                        510,
                        511,
                        511,
                        513,
                        514,
                        514,
                        514,
                        514,
                        514,
                        514,
                        520,
                        521,
                        524,
                        524,
                        525,
                        525,
                        525,
                        525,
                        526,
                        527,
                        527,
                        528,
                        529,
                        529,
                        529,
                        529,
                        530,
                        533,
                        533,
                        534,
                        534,
                        535,
                        535,
                        535,
                        536,
                        537,
                        539,
                        539,
                        540,
                        542,
                        542,
                        545,
                        546,
                        547,
                        548,
                        551,
                        551,
                        552,
                        553,
                        555,
                        555,
                        555,
                        556,
                        559,
                        560,
                        562,
                        564,
                        564,
                        564,
                        565,
                        565,
                        565,
                        570,
                        571,
                        571,
                        573,
                        573,
                        574,
                        574,
                        576,
                        576,
                        581,
                        581,
                        581,
                        583,
                        584,
                        584,
                        587,
                        588,
                        589,
                        589,
                        589,
                        590,
                        590,
                        591,
                        593,
                        593,
                        595,
                        595,
                        596,
                        597,
                        597,
                        598,
                        598,
                        600,
                        600,
                        604,
                        605,
                        605,
                        606,
                        606,
                        607,
                        607,
                        608,
                        608,
                        609,
                        609,
                        609,
                        610,
                        615,
                        615,
                        616,
                        617,
                        617,
                        621,
                        622,
                        622,
                        623,
                        623,
                        623,
                        624,
                        624,
                        625,
                        626,
                        628,
                        631,
                        632,
                        632,
                        634,
                        634,
                        635,
                        636,
                        636,
                        636,
                        636,
                        637,
                        637,
                        641,
                        642,
                        644,
                        646,
                        647,
                        648,
                        648,
                        648,
                        649,
                        650,
                        652,
                        654,
                        655,
                        655,
                        655,
                        656,
                        656,
                        656,
                        660,
                        660,
                        660,
                        661,
                        661,
                        662,
                        662,
                        664,
                        666,
                        666,
                        667,
                        668,
                        668,
                        668,
                        668,
                        669,
                        670,
                        670,
                        671,
                        671,
                        672,
                        673,
                        673,
                        673,
                        676,
                        677,
                        677,
                        678,
                        679,
                        680,
                        680,
                        680,
                        681,
                        682,
                        683,
                        686,
                        688,
                        689,
                        689,
                        689,
                        692,
                        692,
                        692,
                        692,
                        693,
                        695,
                        695,
                        696,
                        697,
                        698,
                        699,
                        699,
                        702,
                        703,
                        703,
                        704,
                        704,
                        705,
                        705,
                        705,
                        706,
                        707,
                        707,
                        708,
                        708,
                        710,
                        710,
                        710,
                        710,
                        711,
                        712,
                        713,
                        714,
                        714,
                        715,
                        716,
                        716,
                        717,
                        717,
                        720,
                        720,
                        721,
                        721,
                        723,
                        724,
                        724,
                        725,
                        726,
                        726,
                        728,
                        730,
                        730,
                        731,
                        732,
                        732,
                        732,
                        734,
                        736,
                        738,
                        738,
                        743,
                        743,
                        743,
                        744,
                        746,
                        746,
                        746,
                        747,
                        749,
                        750,
                        751,
                        751,
                        751,
                        751,
                        752,
                        753,
                        753,
                        753,
                        754,
                        755,
                        756,
                        757,
                        758,
                        759,
                        759,
                        759,
                        760,
                        760,
                        760,
                        760,
                        761,
                        762,
                        763,
                        763,
                        766,
                        766,
                        768,
                        768,
                        769,
                        769,
                        770,
                        770,
                        770,
                        771,
                        771,
                        771,
                        772,
                        775,
                        776,
                        777,
                        778,
                        780,
                        780,
                        781,
                        784,
                        785,
                        785,
                        786,
                        786,
                        787,
                        788,
                        788,
                        789,
                        790,
                        790,
                        792,
                        794,
                        795,
                        796,
                        796,
                        796,
                        796,
                        798,
                        799,
                        801,
                        803,
                        803,
                        805,
                        805,
                        805,
                        806,
                        807,
                        808,
                        810,
                        810,
                        812,
                        812,
                        813,
                        814,
                        814,
                        814,
                        814,
                        814,
                        814,
                        815,
                        815,
                        817,
                        817,
                        818,
                        819,
                        819,
                        819,
                        821,
                        822,
                        824,
                        825,
                        825,
                        825,
                        826,
                        827,
                        830,
                        830,
                        831,
                        831,
                        831,
                        833,
                        834,
                        836,
                        838,
                        839,
                        839,
                        840,
                        841,
                        842,
                        843,
                        850,
                        850,
                        852,
                        852,
                        853,
                        855,
                        856,
                        856,
                        857,
                        858,
                        859,
                        859,
                        861,
                        862,
                        864,
                        867,
                        869,
                        869,
                        872,
                        873,
                        873,
                        874,
                        875,
                        876,
                        876,
                        877,
                        877,
                        877,
                        877,
                        879,
                        880,
                        881,
                        882,
                        882,
                        882,
                        884,
                        885,
                        885,
                        887,
                        889,
                        889,
                        889,
                        889,
                        892,
                        894,
                        895,
                        896,
                        896,
                        896,
                        899,
                        899,
                        900,
                        901,
                        902,
                        902,
                        903,
                        907,
                        907,
                        911,
                        915,
                        915,
                        915,
                        916,
                        916,
                        916,
                        917,
                        918,
                        918,
                        920,
                        920,
                        920,
                        921,
                        921,
                        921,
                        923,
                        925,
                        928,
                        929,
                        931,
                        932,
                        933,
                        935,
                        935,
                        936,
                        936,
                        937,
                        938,
                        938,
                        940,
                        940,
                        941,
                        942,
                        943,
                        943,
                        944,
                        946,
                        948,
                        949,
                        949,
                        951,
                        953,
                        955,
                        955,
                        958,
                        958,
                        958,
                        960,
                        961,
                        963,
                        963,
                        964,
                        965,
                        965,
                        965,
                        966,
                        969,
                        969,
                        973,
                        973,
                        974,
                        975,
                        975,
                        976,
                        981,
                        985,
                        985,
                        985,
                        985,
                        985,
                        987,
                        987,
                        989,
                        990,
                        991,
                        992,
                        993,
                        993,
                        994,
                        996,
                        996,
                        998,
                        1000,
                        1000,
                    ]
                ),
            ],
            "expected": [4, 126, 302352054],
        },
    ]


if __name__ == "__main__":
    unittest.main()
