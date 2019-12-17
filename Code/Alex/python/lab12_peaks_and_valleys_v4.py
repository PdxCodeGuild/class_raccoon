'''
Visualization of test data:

Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V
Example I/O:

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]


Version 4 (optional)

Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.

                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
'''
